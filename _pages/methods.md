---
layout: page
title: Methods
description: Follow the code from thermal-mechanical reference fields to inherent strain optimization and component prediction.
permalink: /methods/
nav: true
nav_order: 2
---

{% assign hub = site.data.residual_stress_hub %}

<div class="rsh rsh-page-brand">
<section class="rsh-hero rsh-hero-with-background" aria-label="Residual Stress Hub">
<img class="rsh-hero-background" src="{{ hub.hero_background | relative_url }}" alt="" aria-hidden="true">
<a class="rsh-hero-brand rsh-site-title" href="{{ '/' | relative_url }}" aria-label="Residual Stress Hub home">
<img class="rsh-logo" src="{{ hub.logo | relative_url }}" alt="" aria-hidden="true" width="200" height="160">
<span class="rsh-brand-name"><span class="rsh-stress-name">Residual Stress</span> <span class="rsh-hub-name">Hub</span></span>
</a>
</section>
</div>

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">

<div class="rsh" markdown="1">

The workflow connects a local thermal-mechanical reference simulation, inherent strain identification, and a full-component prediction. Read it from inputs to outputs: each stage prepares the data needed by the next.
{: .rsh-readable}

| Stage                          | Input                                                     | Output                                                   |
| :----------------------------- | :-------------------------------------------------------- | :------------------------------------------------------- |
| Thermal-mechanical reference   | Local mesh, scan path, process and material data          | Cooled displacement and stress fields                    |
| Inherent strain identification | Reference fields and the same local mesh                  | Optimized inherent strain vector                         |
| Component prediction           | Identified strain, component mesh and activation sequence | Residual stress and deformation before and after release |

[Reference simulation](#thermo-mechanical) · [Run the workflow](#run-the-workflow) · [Inside the optimization](#inside-the-optimization) · [Read the results](#read-the-results)

<section class="rsh-guide-section" id="thermo-mechanical" aria-labelledby="thermo-mechanical-title" markdown="1">

## Full thermal-mechanical analysis {#thermo-mechanical-title}

The reference model resolves the moving heat source and the thermal cycles during deposition and cooling. Temperature-dependent elastic and plastic properties connect this temperature history to residual stress and deformation. In the optimization workflow, this detailed calculation is performed on a small representative domain.

### Follow the thermal-mechanical loop

`am_solver/run.py` starts the calculation; `am_solver/thermo_mech/simulation.py` advances the process history.

1. Activate the material reached by the deposition sequence and update the heat-source position.
2. Solve the transient heat equation for the new temperature field.
3. At mechanical updates, pass temperature and phase changes to the constitutive model, solve equilibrium, and commit stress and plastic history.
4. Continue through deposition and cooling, then export the reference displacement and stress fields.

The heat balance is

$$
\rho C_{\mathrm{p}}(T)\dot T
-\nabla\!\cdot\!\bigl(k(T)\nabla T\bigr)
=Q_{\mathrm{v}}-\rho L\dot f_{\mathrm{l}}.
$$

Here $Q_{\mathrm{v}}$ is the moving volumetric heat source, $L$ is latent heat, and $f_{\mathrm{l}}$ is the liquid fraction. Convection and radiation enter through the boundary flux. `thermal_problem.py` defines the thermal kernels; `plasticity_problem.py` defines the temperature-dependent mechanical response.

<details markdown="1">
<summary><strong>Thermal weak form</strong></summary>

On the active domain $\Omega$, let $w$ vanish on prescribed-temperature boundaries. One backward-Euler step satisfies

$$
\begin{aligned}
0={}&\int_\Omega w\rho C_{\mathrm{p}}(T^{n+1})
\frac{T^{n+1}-T^n}{\Delta t}\,\mathrm{d}\Omega\\
&+\int_\Omega \nabla w\cdot k(T^n)\nabla T^{n+1}\,\mathrm{d}\Omega\\
&-\int_\Omega wQ_{\mathrm{v}}^{n+1}\,\mathrm{d}\Omega
+\int_\Omega w\rho L\frac{f_{\mathrm{l}}^{n+1}-f_{\mathrm{l}}^n}{\Delta t}\,\mathrm{d}\Omega\\
&-\int_{\Gamma_q}w\bar q_{\mathrm{in}}\,\mathrm{d}\Gamma .
\end{aligned}
$$

The inward flux $\bar q_{\mathrm{in}}$ is negative for heat loss. The implementation evaluates conductivity at the previous temperature and heat capacity at the current temperature. This separates the storage, conduction, source, phase-change, and boundary contributions to the thermal residual.

</details>

**What passes to identification?** The final cooled reference contains nodal displacement and cell stress. The orchestrator selects the highest-numbered `step_*.vtu` unless a reference file is supplied explicitly. Complete the cooling stage in `am.yaml` so that this file represents the state being matched.

</section>

<section class="rsh-guide-section" id="inherent-strain" aria-labelledby="inherent-strain-title" markdown="1">

## Optimization-based inherent strain analysis {#inherent-strain-title}

We replace repeated thermal cycles at the component scale with a calibrated inherent strain. The local reference supplies the target fields; a layerwise mechanical model identifies the strain that reproduces them. The resulting vector is then transferred to the full component.

### Run the workflow {#run-the-workflow}

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

### Know which file controls each step

`opt_solver/run.py` orchestrates the stages. The case directory holds the physical inputs; the root `solver_config.yaml` supplies the shared numerical solver settings.

| Case file           | What to read or change                                                                                                  |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| `config.yaml`       | Mesh paths, output directory, stage overrides, and reference displacement conversion                                    |
| `am.yaml`           | Scan path, power $P$, speed $v$, heat-source dimensions, thermal boundaries, and temperature-dependent material data    |
| `optimization.yaml` | Room-temperature material model, strain variables and bounds, regions of interest, loss weights, and optimizer settings |
| `forward.yaml`      | Component layer activation, inherent strain application, constraints, release, and postprocessing                       |

The orchestrator writes the effective stage inputs to `generated_configs/`. These include resolved mesh paths and injected solver settings, so they show exactly what each solver receives.

**The handoff matters:** the reference and identification models share node coordinates, connectivity, and ordering. `load_reference_data()` checks this correspondence; it does not interpolate between meshes. Reference displacements stored in mm are converted to m with `reference.displacement_scale_to_m: 0.001`.

### Define the strain to identify

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

### Understand one mechanical solve

Inherent strain is a prescribed stress-free strain. It changes the constitutive response of newly deposited material. For a virtual displacement $\mathbf v$ that vanishes on the displacement boundary, equilibrium requires

$$
\int_\Omega \boldsymbol\varepsilon(\mathbf v):\boldsymbol\sigma\,\mathrm{d}\Omega
=\ell(\mathbf v),
\qquad
\boldsymbol\varepsilon(\mathbf v)=\operatorname{sym}\nabla\mathbf v,
$$

where $\ell(\mathbf v)$ is the virtual work of body forces and boundary tractions. JAX-FEM assembles this residual from the constitutive kernels in `IS_solver/inherent_solver/problem.py`.

For an elastic illustration, substituting $\boldsymbol\sigma=\mathbb C:(\boldsymbol\varepsilon(\mathbf u)-\boldsymbol\varepsilon^{\ast})$ gives

$$
\begin{aligned}
\int_\Omega \boldsymbol\varepsilon(\mathbf v):\mathbb C:
\boldsymbol\varepsilon(\mathbf u)\,\mathrm{d}\Omega
={}&\ell(\mathbf v)\\
&+\int_\Omega \boldsymbol\varepsilon(\mathbf v):\mathbb C:
\boldsymbol\varepsilon^{\ast}\,\mathrm{d}\Omega .
\end{aligned}
$$

This explains the equivalent strain load. **The implemented identification solver is incremental elastoplastic:** it activates layers, applies strain increments to newly activated cells, and retains stress and plastic history between increments.

<details markdown="1">
<summary><strong>Layer activation and constitutive update</strong></summary>

For a newly activated cell, an increment applies $\Delta\boldsymbol\varepsilon^{\ast}=\gamma_m\boldsymbol\varepsilon^{\ast}$, with $\sum_m\gamma_m=1$. Other cells receive no additional inherent strain in that activation. Identification uses one loading increment per layer; component loading can be subdivided. A configured base region can also receive strain at the first increment.

The elastic trial stress is

$$
\begin{aligned}
\Delta\boldsymbol\varepsilon^{k+1}
&=\operatorname{sym}\!\left(\nabla\mathbf u^{k+1}-\nabla\mathbf u^k\right),\\
\boldsymbol\sigma_{\mathrm{trial}}^{k+1}
&=\boldsymbol\sigma^k+\mathbb C:\!\left(
\Delta\boldsymbol\varepsilon^{k+1}
-\Delta\boldsymbol\varepsilon^{\ast,k+1}\right).
\end{aligned}
$$

A $J_2$ return map with isotropic hardening updates the constitutive response. After equilibrium converges, `update_stress_strain()` commits stress, accumulated plastic strain, and the displacement-gradient history for the next layer.

</details>

### Inside the optimization {#inside-the-optimization}

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

### What does the loss measure?

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
\begin{aligned}
\mathcal L_{\mathrm{vm}}&=\frac{1}{N_c}\sum_{e=1}^{N_c}
\left(\frac{\sigma_{\mathrm{vm},e}^{\mathrm{diag}}
-\widehat\sigma_{\mathrm{vm},e}^{\mathrm{diag}}}{s_{\mathrm{vm}}}\right)^2,\\
\mathcal L_U&=\frac{1}{N_u}\sum_{a=1}^{N_u}
\left(\frac{u_{\mathrm{z},a}-\widehat u_{\mathrm{z},a}}{s_U}\right)^2.
\end{aligned}
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

### How the gradient reaches the strain parameters

Within `run_simulation()`, `ad_wrapper` wraps each mechanical equilibrium solve for implicit differentiation. `jax.value_and_grad(compute_loss_scaled)` evaluates the composed objective and its gradient, which are passed to SciPy's bounded L-BFGS-B optimizer.

Write the layer state as $\mathbf q^{k+1}=F^{k+1}(\mathbf q^k,\boldsymbol\theta)$, including displacement, stress, and plastic history. Its sensitivity follows

$$
\frac{\mathrm{d}\mathbf q^{k+1}}{\mathrm{d}\boldsymbol\theta}
=\frac{\partial F^{k+1}}{\partial\mathbf q^k}
\frac{\mathrm{d}\mathbf q^k}{\mathrm{d}\boldsymbol\theta}
+\frac{\partial F^{k+1}}{\partial\boldsymbol\theta}.
$$

JAX propagates this dependency through the deposition history; the implicit backward solve handles each converged equilibrium. This includes the effect of earlier layers on the final loss. The activation schedule remains fixed while the inherent strain parameters change.

### Transfer to the component and release

The orchestrator reads `optimization/epsilon_result.json`, inserts the selected vector into `inherent_strain.default` in the generated component configuration, and calls `IS_solver/run.py`. The component solver activates layers and applies the calibrated strain using the room-temperature material model.

After deposition, the release stage changes the configured supports or cut connections and re-equilibrates the existing stress state. It adds no new inherent strain. The resulting displacement includes the deformation caused by stress redistribution during release. Transfer assumes that the local reference is representative of the component's deposition conditions.

### Read the results {#read-the-results}

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

</section>

</div>
