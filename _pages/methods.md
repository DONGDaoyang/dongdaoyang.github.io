---
layout: page
title: Methods
description: Follow the code from thermal-mechanical reference fields to inherent strain optimization and component prediction.
permalink: /methods/
nav: true
nav_order: 2
---

{% assign hub = site.data.residual_stress_hub %}

<div class="rsh rsh-page-brand rsh-process-banner" aria-hidden="true">
<img src="{{ hub.page_background | relative_url }}" alt="" aria-hidden="true" width="2172" height="724" fetchpriority="high">
</div>

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url | bust_file_cache }}">

<div class="rsh" markdown="1">

Both methods use finite elements to enforce mechanical equilibrium on the currently active material domain. Full thermal-mechanical analysis also resolves heat transfer and temperature-driven inelastic deformation. Inherent-strain analysis replaces those thermal cycles with a calibrated strain field. The sections below use the same structure so that their common mechanics and different loading models can be compared directly.
{: .rsh-readable}

| Method                                      | Fields solved                                 | Source of residual stress                                       | Typical use                                                  |
| :------------------------------------------ | :-------------------------------------------- | :-------------------------------------------------------------- | :----------------------------------------------------------- |
| Full thermal-mechanical analysis            | Temperature and displacement                  | Constrained thermal expansion, plastic deformation, and cooling | Process-resolved prediction or a local reference calculation |
| Optimization-based inherent strain analysis | Displacement, with prescribed inherent strain | Constrained application of the calibrated strain                | Efficient component prediction after local calibration       |

[Thermal-mechanical method](#thermo-mechanical) · [Inherent-strain method](#inherent-strain) · [Run the workflow](#run-the-workflow) · [Optimization details](#inside-the-optimization)

<section class="rsh-guide-section" id="thermo-mechanical" aria-labelledby="thermo-mechanical-title" markdown="1">

## Full thermal-mechanical analysis {#thermo-mechanical-title}

### Model and weak forms {#thermal-weak-forms}

Let $\Omega_a(t)$ denote the activated material domain. Find temperature $T\in W_D$ and displacement $\mathbf u\in V_D$ satisfying the prescribed values on $\Gamma_T$ and $\Gamma_u$. The scalar test space $W_0$ and vector test space $V_0$ contain $H^1$ functions that vanish on their respective prescribed-value boundaries. Small-strain, quasi-static mechanics uses $\boldsymbol\varepsilon(\mathbf v)=\operatorname{sym}\nabla\mathbf v$.

The thermal weak form is

<div class="rsh-equation" markdown="1" tabindex="0" role="region" aria-label="Thermal weak form">

$$
\int_{\Omega_a}w\rho\bigl(c_p(T)\dot T+L\dot f_L(T)\bigr)\,\mathrm d\Omega+\int_{\Omega_a}\nabla w\cdot k(T)\nabla T\,\mathrm d\Omega=\int_{\Omega_a}wQ_v\,\mathrm d\Omega+\int_{\Gamma_q}w\bar q_{\mathrm{in}}\,\mathrm d\Gamma\quad\forall w\in W_0.
$$

</div>

Here $\rho$ is density, $c_p$ is specific heat, $k$ is conductivity, $L$ is latent heat, and $f_L$ is liquid fraction. $Q_v$ is volumetric heating. The net inward flux $\bar q_{\mathrm{in}}$ includes applicable surface heating, convection, and radiation, with heat loss contributing a negative inward flux; it may depend on temperature. The sensible-heat and latent-heat terms account for energy storage. Time discretization and quadrature turn this statement into the thermal finite-element residual at each step.

The mechanical weak form is

<div class="rsh-equation" markdown="1" tabindex="0" role="region" aria-label="Thermal-mechanical equilibrium weak form">

$$
\int_{\Omega_a}\boldsymbol\varepsilon(\mathbf v):\boldsymbol\sigma\,\mathrm d\Omega=\int_{\Omega_a}\mathbf v\cdot\mathbf b\,\mathrm d\Omega+\int_{\Gamma_t}\mathbf v\cdot\bar{\mathbf t}\,\mathrm d\Gamma\quad\forall\mathbf v\in V_0.
$$

</div>

$\mathbf b$ is body force per unit volume and $\bar{\mathbf t}$ is prescribed traction. The constitutive update supplies $\boldsymbol\sigma$ from the displacement increment, temperature change, and stored plastic history. Thermal strain provides the temperature-driven stress-free strain. The material properties and hardening response follow the selected case.

### Element activation

The substrate is active initially. Deposition activates new cells as the prescribed scan reaches them, expanding $\Omega_a(t)$. Active cells contribute to the heat-capacity, conduction, and mechanical residuals. Masks suppress inactive-cell contributions, and constraints on inactive degrees of freedom keep the algebraic problem well posed.

When material is added, the exposed thermal faces and applicable heat-loss boundaries are updated. Newly activated material receives its configured initial state. Previously deposited cells retain their temperature, stress, and internal-variable history, so later scans can reheat and mechanically load the existing build.

### Solution procedure

1. Update the heat-source position, activation mask, and exposed surfaces.
2. Solve the thermal weak form over the active mesh for the next temperature field.
3. Pass temperature changes to the mechanical constitutive update and solve the mechanical weak form at the configured mechanical updates.
4. Commit the converged stress and plastic history, then continue through deposition and cooling.

The coupling is staggered: temperature drives the mechanical calculation. The local calculation used for inherent-strain calibration follows this same sequence before its cooled fields are exported.

### Cutting and stress release

Release starts from the final constrained state after the prescribed cooling stage. The selected anchors or support connections are removed while the retained constraints remain active. Newly exposed cut faces carry zero prescribed traction unless a different load is specified. If cutting removes cells, the remaining domain and its boundary are updated as well.

The mechanical weak form is then solved again with the inherited stress and plastic state and the revised constraints. Displacement changes as stresses redistribute to satisfy the new equilibrium. Residual stress can remain in the released part. No additional heat cycle is needed for this mechanical release step. Report the total post-release displacement separately from the release increment $\Delta\mathbf u_{\mathrm{release}}=\mathbf u_{\mathrm{after}}-\mathbf u_{\mathrm{before}}$.

### Implementation and results

| Entry point                           | Role                                                           |
| :------------------------------------ | :------------------------------------------------------------- |
| `am_solver/run.py`                    | Start the configured thermal-mechanical case                   |
| `am_solver/thermo_mech/simulation.py` | Advance scanning, activation, cooling, and optional springback |
| `thermal_problem.py`                  | Assemble thermal storage, conduction, and boundary terms       |
| `plasticity_problem.py`               | Supply the temperature-dependent constitutive response         |

The saved fields contain temperature, displacement, stress, and the configured history variables. For calibration, complete the cooling stage in `am.yaml` before selecting the reference. The orchestrator selects the highest-numbered `step_*.vtu` unless a reference file is supplied explicitly. Release-enabled cases also export the post-release fields and displacement increment.

</section>

<section class="rsh-guide-section" id="inherent-strain" aria-labelledby="inherent-strain-title" markdown="1">

## Optimization-based inherent strain analysis {#inherent-strain-title}

### Model and weak forms {#inherent-weak-forms}

On the current activated domain $\Omega_a$, find displacement $\mathbf u\in V_D$ satisfying the prescribed displacements. For every $\mathbf v\in V_0$, with the same virtual strain and boundary-work definitions as above, the standard mechanical weak form is

<div class="rsh-equation" markdown="1" tabindex="0" role="region" aria-label="Inherent-strain equilibrium weak form">

$$
\int_{\Omega_a}\boldsymbol\varepsilon(\mathbf v):\boldsymbol\sigma\,\mathrm d\Omega=\int_{\Omega_a}\mathbf v\cdot\mathbf b\,\mathrm d\Omega+\int_{\Gamma_t}\mathbf v\cdot\bar{\mathbf t}\,\mathrm d\Gamma\quad\forall\mathbf v\in V_0.
$$

</div>

The loading model enters through the stress-free inherent strain $\boldsymbol\varepsilon^\ast$. For a purely elastic material, $\boldsymbol\sigma=\mathbb C:(\boldsymbol\varepsilon(\mathbf u)-\boldsymbol\varepsilon^\ast)$. The implemented solver instead uses incremental elastoplastic updates and carries stress and plastic history between increments. Its calibrated strain represents the net effect of the local thermal cycles, so the component calculation does not solve a heat-transfer problem.

<details markdown="1">
<summary><strong>Strain parameters and the elastic equivalent load</strong></summary>

The prescribed inherent strain is diagonal:

$$
\boldsymbol\varepsilon^{\ast}
=\operatorname{diag}\!\left(
\varepsilon_{\mathrm{xx}}^{\ast},
\varepsilon_{\mathrm{yy}}^{\ast},
\varepsilon_{\mathrm{zz}}^{\ast}\right).
$$

With `tie_xy: true`, the optimizer has two independent variables:

$$
\boldsymbol\theta=
\left[\varepsilon_{\parallel}^{\ast},\,
\varepsilon_{\mathrm{zz}}^{\ast}\right],
\qquad
\varepsilon_{\mathrm{xx}}^{\ast}
=\varepsilon_{\mathrm{yy}}^{\ast}
=\varepsilon_{\parallel}^{\ast}.
$$

`expand_inherent_strain_parameters()` expands these two entries into the three-component vector used by the mechanics. Bounds and initial values belong to the case configuration. The optimizer works with scaled variables $\mathbf p$, with $\boldsymbol\theta=\mathbf s\odot\mathbf p$; `param_scale` defines $\mathbf s$.

For the elastic illustration, write $\ell(\mathbf v)=\int_{\Omega_a}\mathbf v\cdot\mathbf b\,\mathrm d\Omega+\int_{\Gamma_t}\mathbf v\cdot\bar{\mathbf t}\,\mathrm d\Gamma$. Substitution of the elastic constitutive relation gives

<div class="rsh-equation" markdown="1" tabindex="0" role="region" aria-label="Elastic inherent-strain equivalent weak form">

$$
\int_{\Omega_a}\boldsymbol\varepsilon(\mathbf v):\mathbb C:\boldsymbol\varepsilon(\mathbf u)\,\mathrm d\Omega=\ell(\mathbf v)+\int_{\Omega_a}\boldsymbol\varepsilon(\mathbf v):\mathbb C:\boldsymbol\varepsilon^\ast\,\mathrm d\Omega.
$$

</div>

This equivalent strain load explains the role of $\boldsymbol\varepsilon^\ast$ in the finite-element residual. The incremental elastoplastic implementation evaluates stress through its constitutive update rather than assuming a globally linear elastic response.

</details>

### Element activation

A fixed layer schedule expands the active domain. Newly activated cells receive the prescribed inherent-strain increment $\Delta\boldsymbol\varepsilon^\ast=\gamma_m\boldsymbol\varepsilon^\ast$, with $\sum_m\gamma_m=1$ over the loading subdivisions for that activation. A configured base region may also receive strain at the first increment.

Previously active cells retain their stress and plastic state and respond to the new layer through equilibrium. Their deposited inherent strain is not applied again at every subsequent layer. Identification uses one loading increment per layer, while component loading can be subdivided. Inactive cells and degrees of freedom are handled by the activation masks and associated constraints.

### Solution procedure

1. Obtain cooled local displacement and stress fields from the thermal-mechanical reference model.
2. For each trial strain vector, replay the layer-activation schedule and solve the mechanical weak form, retaining history within that trial.
3. Compare the final local fields with the reference and use differentiable finite elements to supply the objective gradient to bounded L-BFGS-B.
4. Transfer the selected strain to the component model and solve its layerwise deposition sequence with the configured room-temperature material model.

Each trial starts from the same unloaded local state. The thermal reference is calculated once and held fixed during optimization. The activation schedule also remains fixed as the strain parameters change.

<details id="inside-the-optimization" markdown="1">
<summary><strong>Optimization and differentiation details</strong></summary>

#### Calibration data flow

Start reading `IS_solver/optimization/inherent_strain_optimization.py`. Its functions follow the data flow:

| Function                       | Role                                                       |
| :----------------------------- | :--------------------------------------------------------- |
| `load_reference_data()`        | Load and check the target displacement and stress fields   |
| `build_roi_indices()`          | Select the cells and nodes used in the loss                |
| `build_problem_and_schedule()` | Prepare layer activation and mechanical problems           |
| `run_simulation()`             | Replay the entire deposition sequence for one trial strain |
| `run_optimization()`           | Compose the loss, compute gradients, and call L-BFGS-B     |

The following is **schematic pseudocode** for the nested loops; it is a reading guide rather than a runnable script.

```text
Load the reference fields and select regions of interest.
Build the fixed layer-activation schedule.

For each trial parameter vector requested by L-BFGS-B:
    Scale the parameters and expand the strain vector.
    Reset displacement, stress, and plastic history to zero.

    For each layer in the schedule:
        Activate the new cells.
        Apply their inherent strain increment.
        Solve mechanical equilibrium with ad_wrapper.
        Commit stress and plastic history for the next layer.

    Compare the final fields with the reference.
    Differentiate the loss through the layer history.
    Return the loss and parameter gradient to L-BFGS-B.

Save the selected strain vector and comparison fields.
Transfer the vector to the component configuration.
```

The history reset belongs **outside the layer loop and inside each trial evaluation**. Layers within one trial share history; separate parameter trials start from the same unloaded state. The thermal reference is computed once and stays fixed during optimization.

#### Loss and comparison regions

The objective combines four normalized terms:

$$
\mathcal L= w_\sigma\mathcal L_\sigma
+w_{\mathrm{vm}}\mathcal L_{\mathrm{vm}}
+w_U\mathcal L_U+w_C\mathcal L_C.
$$

| Term                       | Comparison                                                                                         | Normalization                                 |
| :------------------------- | :------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| $\mathcal L_\sigma$        | $\sigma_{\mathrm{xx}}$, $\sigma_{\mathrm{yy}}$, $\sigma_{\mathrm{zz}}$ in the active stress region | Material initial yield strength               |
| $\mathcal L_{\mathrm{vm}}$ | Equivalent stress calculated from the three normal stresses                                        | Reference RMS, with a 1 MPa floor             |
| $\mathcal L_U$             | Top-region vertical displacement $u_{\mathrm{z}}$                                                  | Reference RMS, with a $10^{-12}$ m floor      |
| $\mathcal L_C$             | Mean lateral relative contraction in the $x$ and $y$ directions                                    | Reference contraction, with a $10^{-5}$ floor |

The Bridge configuration uses $(w_\sigma,w_{\mathrm{vm}},w_U,w_C)=(2,1,1,1)$. The contraction term is a one-sided penalty with a target factor of 1.4. These values are configurable; the formulas below describe this setting.

<details markdown="1">
<summary><strong>Loss definitions and regions of interest</strong></summary>

A hat denotes a reference value. With $N_c$ active cells in the stress region, the normal-stress loss is

$$
\mathcal L_\sigma=\frac{1}{N_c}
\sum_{e=1}^{N_c}\sum_{i\in\{\mathrm{xx},\mathrm{yy},\mathrm{zz}\}}
\left(\frac{\sigma_{i,e}-\widehat\sigma_{i,e}}{\sigma_{\mathrm{y},0}}\right)^2.
$$

The three component errors are summed without a further division by three. The equivalent stress used in the matching term is

$$
\sigma_{\mathrm{vm}}^{\mathrm{diag}}
=\sqrt{\frac{
(\sigma_{\mathrm{xx}}-\sigma_{\mathrm{yy}})^2+
(\sigma_{\mathrm{yy}}-\sigma_{\mathrm{zz}})^2+
(\sigma_{\mathrm{zz}}-\sigma_{\mathrm{xx}})^2}{2}}.
$$

This matching quantity excludes shear stresses. It differs from the full tensor invariant used in the plasticity model.

$$
\mathcal L_{\mathrm{vm}}=\frac{1}{N_c}\sum_{e=1}^{N_c}
\left(\frac{\sigma_{\mathrm{vm},e}^{\mathrm{diag}}
-\widehat\sigma_{\mathrm{vm},e}^{\mathrm{diag}}}{s_{\mathrm{vm}}}\right)^2.
$$

$$
\mathcal L_U=\frac{1}{N_u}\sum_{a=1}^{N_u}
\left(\frac{u_{\mathrm{z},a}-\widehat u_{\mathrm{z},a}}{s_U}\right)^2.
$$

Here $N_u$ counts the selected top-region nodes. Each RMS normalization is calculated from the corresponding reference values and held fixed during optimization.

For direction $i\in\{x,y\}$, pair opposite boundary nodes and define positive contraction by

$$
c_i=-\frac{\left\langle u_i^{\mathrm{high}}-u_i^{\mathrm{low}}\right\rangle}{d_i},
\qquad c=\frac{c_x+c_y}{2},
$$

where $d_i$ is the undeformed span. Set $\widehat c_+=[\max(\widehat c_x,0)+\max(\widehat c_y,0)]/2$ and $s_C=\max(\widehat c_+,10^{-5})$. The configured penalty is

$$
\mathcal L_C=\left[\max\!\left(\frac{1.4\widehat c_+-c}{s_C},0\right)\right]^2.
$$

Thus a trial is penalized for falling below the contraction target. `relative_contraction.py` constructs the node pairs and evaluates this term.

</details>

#### Differentiating the layer history

Within `run_simulation()`, `ad_wrapper` wraps each mechanical equilibrium solve for implicit differentiation. `jax.value_and_grad(compute_loss_scaled)` evaluates the composed objective and its gradient, which are passed to SciPy's bounded L-BFGS-B optimizer.

Write the layer state as $\mathbf q^{k+1}=F^{k+1}(\mathbf q^k,\boldsymbol\theta)$, including displacement, stress, and plastic history. Its sensitivity follows

$$
\frac{\mathrm{d}\mathbf q^{k+1}}{\mathrm{d}\boldsymbol\theta}
=\frac{\partial F^{k+1}}{\partial\mathbf q^k}
\frac{\mathrm{d}\mathbf q^k}{\mathrm{d}\boldsymbol\theta}
+\frac{\partial F^{k+1}}{\partial\boldsymbol\theta}.
$$

JAX propagates this dependency through the deposition history; the implicit backward solve handles each converged equilibrium. This includes the effect of earlier layers on the final loss. The activation schedule remains fixed while the inherent strain parameters change.

</details>

### Cutting and stress release

After component deposition, release modifies the selected supports, interface connections, or retained-cell set. The solver carries the pre-cut displacement, stress, and plastic state into the released configuration, applies traction-free conditions on the new free surfaces, and solves the same mechanical weak form again.

The calibrated inherent strain remains the deposition history of the retained material. The cutting step applies no new inherent strain. Stress redistribution produces the post-cut deformation, with each remaining support continuing to constrain the part. Compare the total released displacement and its change from the constrained state separately, using the same definition of $\Delta\mathbf u_{\mathrm{release}}$ as in the thermal-mechanical method.

### Implementation and results {#read-the-results}

The orchestrator reads `optimization/epsilon_result.json`, inserts the selected vector into `inherent_strain.default`, and calls `IS_solver/run.py` for the component. The reference and identification models share node coordinates, connectivity, and ordering. `load_reference_data()` checks this correspondence without interpolating between meshes. Reference displacements stored in mm are converted to m with `reference.displacement_scale_to_m: 0.001`.

<details id="run-the-workflow" markdown="1">
<summary><strong>Run the workflow and locate its files</strong></summary>

From the solver project root, in an environment with JAX, JAX-FEM, MeshIO, SciPy, PyYAML, and the configured linear solver:

```bash
# Resolve inputs and write stage configurations without solving.
python opt_solver/run.py bridge --dry-run

# Reference simulation → identification → component prediction.
python opt_solver/run.py bridge
```

To reuse completed stages:

```bash
python opt_solver/run.py bridge --from-stage optimization
python opt_solver/run.py bridge --from-stage forward
```

`--from-stage` reuses preceding outputs; it does not resume inside a time step or an optimizer iteration. The first command needs an existing reference field, and the second needs `epsilon_result.json`.

#### Configuration files

`opt_solver/run.py` orchestrates the stages. The case directory holds the physical inputs; the root `solver_config.yaml` supplies the shared numerical solver settings.

| Case file           | What to read or change                                                                                                  |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| `config.yaml`       | Mesh paths, output directory, stage overrides, and reference displacement conversion                                    |
| `am.yaml`           | Scan path, power $P$, speed $v$, heat-source dimensions, thermal boundaries, and temperature-dependent material data    |
| `optimization.yaml` | Room-temperature material model, strain variables and bounds, regions of interest, loss weights, and optimizer settings |
| `forward.yaml`      | Component layer activation, inherent strain application, constraints, release, and postprocessing                       |

The orchestrator writes the effective stage inputs to `generated_configs/`. These include resolved mesh paths and injected solver settings, so they show exactly what each solver receives.

#### Output files

Outputs are organized under `opt_output/<case>/`:

| Output                             | What it tells you                                            |
| :--------------------------------- | :----------------------------------------------------------- |
| `generated_configs/`               | Effective inputs for each enabled stage                      |
| `am/vtk/step_*.vtu`                | Thermal-mechanical history and reference fields              |
| `optimization/epsilon_result.json` | Selected inherent strain vector and optimizer report         |
| `optimization/vtk/`                | Identified mechanical fields and comparison errors           |
| `forward/`                         | Component prediction, release, and configured postprocessing |
| `workflow_result.json`             | Stage completion and paths to the workflow artifacts         |

Read the optimizer status together with the strain values: the case's `require_success` setting controls whether a result that reaches the iteration limit can proceed to component prediction. To understand a mismatch, inspect the reference and identification fields in the configured regions before interpreting the component result.

</details>

</section>

Variational background: [transient heat transfer](https://jsdokken.com/dolfinx-tutorial/chapter2/heat_equation.html) · [mechanical equilibrium](https://jsdokken.com/dolfinx-tutorial/chapter2/linearelasticity.html).
{: .rsh-note}

</div>
