const { test, expect } = require("@playwright/test");

const routes = [
  "/",
  "/benchmarks/",
  "/projects/",
  "/benchmarks/cantilever/",
  "/benchmarks/example-1/",
  "/benchmarks/double-cantilever/",
  "/benchmarks/thin-wall/",
  "/benchmarks/bridge/",
  "/benchmarks/single-track/",
  "/methods/",
  "/resources/",
];

async function openPage(page, route) {
  const response = await page.goto(route, { waitUntil: "domcontentloaded" });
  expect(response.status()).toBe(200);
  await expect(page.locator(".rsh, .post > article:has(> #overview)").first()).toBeVisible();
}

for (const theme of ["light", "dark"]) {
  test.describe(`${theme} Hub`, () => {
    test.beforeEach(async ({ page }) => {
      await page.addInitScript((setting) => localStorage.setItem("theme", setting), theme);
    });

    for (const route of routes) {
      test(`shared navigation and working images: ${route}`, async ({ page }) => {
        await openPage(page, route);
        const nav = page.locator("#navbar .nav-link");
        expect((await nav.allTextContents()).map((text) => text.replace(/\(current\)/g, "").trim())).toEqual([
          "Home",
          "Benchmarks",
          "Methods",
          "Resources",
        ]);
        expect(await nav.evaluateAll((links) => links.map((link) => link.getAttribute("href")))).toEqual([
          "/",
          "/benchmarks/",
          "/methods/",
          "/resources/",
        ]);
        await expect(page.locator("#navbar")).not.toContainText(/Albert Einstein|Daoyang Dong/);
        if (route !== "/") {
          const brand = page.locator(".rsh-page-brand");
          await expect(brand).toHaveCount(1);
          if (["/methods/", "/resources/", "/benchmarks/", "/projects/"].includes(route)) {
            await expect(brand).toHaveClass(/rsh-process-banner/);
            await expect(brand).toHaveCSS("background-color", "rgba(0, 0, 0, 0)");
            await expect(brand.locator(".rsh-logo, .rsh-site-title")).toHaveCount(0);
            await expect(brand.locator("img")).toHaveAttribute("src", /additive-manufacturing-banner-transparent\.webp\?v=[a-f0-9]+$/);
            const title = page.locator(".post-header .post-title");
            await expect(title).toHaveText(route === "/methods/" ? "Methods" : route === "/resources/" ? "Resources" : "Benchmarks");
            const titleBox = await title.boundingBox();
            const bannerBox = await brand.boundingBox();
            expect(titleBox.y).toBeGreaterThanOrEqual(bannerBox.y);
            expect(titleBox.y + titleBox.height).toBeLessThanOrEqual(bannerBox.y + bannerBox.height);
            expect(Math.abs(titleBox.x + titleBox.width / 2 - bannerBox.x - bannerBox.width / 2)).toBeLessThanOrEqual(1);
          } else {
            await expect(brand.locator(".rsh-site-title")).toHaveText("Residual Stress Hub");
            await expect(brand.locator(".rsh-site-title")).toHaveAttribute("href", "/");
            await expect(brand.locator(".rsh-logo")).toHaveAttribute("src", /rs-logo-metal\.webp\?v=[a-f0-9]+$/);
            await expect(brand.locator(".rsh-hero-background")).toHaveAttribute("src", /honeycomb-background\.svg\?v=[a-f0-9]+$/);
          }
          for (const image of await brand.locator("img").all()) {
            await expect.poll(() => image.evaluate((element) => element.complete && element.naturalWidth > 0)).toBe(true);
          }
          const brandBox = await brand.boundingBox();
          const pageHeader = await page.locator(".post-header").boundingBox();
          expect(brandBox.y + brandBox.height).toBeLessThanOrEqual(pageHeader.y + 1);
          if (theme === "light" && route === "/benchmarks/") {
            await page.screenshot({ path: `/tmp/rsh-benchmarks-${test.info().project.name}.png` });
          }
        }
        await expect(page.locator("#toc-sidebar")).toHaveCount(0);
        const images = page.locator('.rsh img:not([aria-hidden="true"]), .post > article:has(> #overview) img:not([aria-hidden="true"])');
        for (let i = 0; i < (await images.count()); i++) {
          const image = images.nth(i);
          await image.scrollIntoViewIfNeeded();
          await expect(image).toHaveAttribute("alt", /\S+/);
          await expect.poll(() => image.evaluate((img) => img.complete && img.naturalWidth > 0)).toBe(true);
        }
        for (const grid of await page.locator(".rsh-case-figures").all()) {
          const columns = await grid.evaluate((element) => getComputedStyle(element).gridTemplateColumns.split(" ").length);
          expect(columns).toBe(page.viewportSize().width >= 768 ? 2 : 1);
          const figures = grid.locator(".rsh-case-figure");
          if (columns === 2) {
            for (let i = 0; i + 1 < (await figures.count()); i += 2) {
              const first = await figures.nth(i).boundingBox();
              const second = await figures.nth(i + 1).boundingBox();
              expect(Math.abs(first.y - second.y)).toBeLessThanOrEqual(1);
              expect(second.x).toBeGreaterThan(first.x + first.width);
              const firstImage = await figures.nth(i).locator("img").boundingBox();
              const secondImage = await figures
                .nth(i + 1)
                .locator("img")
                .boundingBox();
              expect(Math.abs(firstImage.y - secondImage.y), `Image tops in ${route}, pair ${i / 2 + 1}`).toBeLessThanOrEqual(1);
            }
          }
        }
        expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(await page.evaluate(() => window.innerWidth + 1));
      });
    }

    test("wide screens use the viewport for galleries, cards and case figures", async ({ page }, testInfo) => {
      test.skip(testInfo.project.name !== "desktop", "Wide-screen checks use the desktop browser.");
      for (const width of [1920, 2560]) {
        await page.setViewportSize({ width, height: 1440 });
        for (const route of ["/", "/benchmarks/", "/benchmarks/cantilever/"]) {
          await openPage(page, route);
          const main = await page.locator('[role="main"]').boundingBox();
          expect(main.width / width).toBeGreaterThan(0.69);
          expect(main.width / width).toBeLessThanOrEqual(0.71);
          expect(main.width).toBeLessThanOrEqual(2201);
          const nav = await page.locator("#navbar > .container").boundingBox();
          expect(Math.abs(nav.x - main.x)).toBeLessThanOrEqual(1);
          expect(Math.abs(nav.width - main.width)).toBeLessThanOrEqual(1);
          if (route === "/") {
            const gallery = page.locator(".rsh-gallery-grid");
            const galleryBox = await gallery.boundingBox();
            expect(galleryBox.width / main.width).toBeGreaterThan(0.95);
            expect(await gallery.evaluate((grid) => getComputedStyle(grid).gridTemplateColumns.split(" ").length)).toBe(4);
            await expect(page.locator(".rsh-welcome")).toHaveCSS("column-count", "1");
          } else if (route === "/benchmarks/") {
            const grid = page.locator(".rsh-grid");
            const gridBox = await grid.boundingBox();
            expect(gridBox.width / main.width).toBeGreaterThan(0.95);
            expect(await grid.evaluate((element) => getComputedStyle(element).gridTemplateColumns.split(" ").length)).toBe(3);
          } else {
            const article = await page.locator(".post > article").boundingBox();
            expect(article.width / main.width).toBeGreaterThan(0.95);
            const figure = await page.locator(".rsh-case-figures img").first().boundingBox();
            expect(figure.width / article.width).toBeGreaterThan(0.45);
            expect(figure.width / article.width).toBeLessThanOrEqual(0.5);
          }
          expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(width + 1);
        }
      }
    });

    test("home brand keeps the RS logo beside its title over a translucent background", async ({ page }, testInfo) => {
      const widths = testInfo.project.name === "desktop" ? [1366, 2560] : [320, 390];
      for (const width of widths) {
        await page.setViewportSize({ width, height: 1100 });
        await openPage(page, "/");
        const logo = page.locator(".rsh-hero .rsh-logo");
        const name = page.locator(".rsh-brand-name");
        const background = page.locator(".rsh-hero-background");
        await expect(logo).toBeVisible();
        await expect(logo).toHaveAttribute("src", /rs-logo-metal\.webp\?v=[a-f0-9]+$/);
        await expect(background).toHaveAttribute("src", /honeycomb-background\.svg\?v=[a-f0-9]+$/);
        await expect.poll(() => logo.evaluate((image) => image.complete && image.naturalWidth > 0)).toBe(true);
        await expect.poll(() => background.evaluate((image) => image.complete && image.naturalWidth > 0)).toBe(true);
        await expect(background).toHaveCSS("opacity", "0.42");
        await expect(background).toHaveAttribute("aria-hidden", "true");
        const markBox = await logo.boundingBox();
        const nameBox = await name.boundingBox();
        expect(markBox.x + markBox.width).toBeLessThanOrEqual(nameBox.x);
        expect(Math.abs(markBox.y + markBox.height / 2 - nameBox.y - nameBox.height / 2)).toBeLessThanOrEqual(1);
        await expect(name).toHaveCSS("white-space", "nowrap");
        await expect(name.locator(".rsh-stress-name")).toHaveCSS("background-image", "none");
        await expect(name.locator(".rsh-stress-name")).toHaveCSS("color", theme === "light" ? "rgb(38, 55, 70)" : "rgb(224, 230, 235)");
        await expect(name.locator(".rsh-hub-name")).toHaveCSS("color", theme === "light" ? "rgb(112, 134, 152)" : "rgb(165, 185, 200)");
        expect(nameBox.x + nameBox.width).toBeLessThanOrEqual(width);
        expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(width + 1);
        await expect(page.locator(".rsh-welcome")).toContainText("Howdy! Welcome to Residual Stress Hub.");
        if (theme === "light" && width === widths[0]) {
          await page.screenshot({ path: `/tmp/rsh-home-${testInfo.project.name}.png` });
        }
      }
    });

    test("home has eight animation slots and all seven supplied animations actually move", async ({ page }) => {
      await openPage(page, "/");
      await expect(page.locator("#hub-title")).toHaveCSS("text-align", "center");
      await expect(page.locator(".rsh-hero .rsh-logo")).toBeVisible();
      await expect.poll(() => page.locator(".rsh-logo").evaluate((image) => image.complete && image.naturalWidth > 0)).toBe(true);
      const welcomeBox = await page.locator(".rsh-welcome").boundingBox();
      const galleryBox = await page.locator(".rsh-gallery").boundingBox();
      expect(galleryBox.y).toBeGreaterThanOrEqual(welcomeBox.y + welcomeBox.height);
      await expect(page.locator(".rsh-gallery-item")).toHaveCount(8);
      expect((await page.locator(".rsh-gallery").innerText()).trim()).toBe("");
      await expect(page.locator(".rsh-animation-placeholder")).toHaveCount(1);
      const animations = page.locator(".rsh-gallery-item img");
      await expect(animations).toHaveCount(7);
      const slots = page.locator(".rsh-gallery-item");
      expect(await slots.evaluateAll((items) => items.map((item) => item.getAttribute("aria-label")))).toEqual([
        "Point heat source",
        "Single track (DED)",
        "Thin-wall (WAAM)",
        "Scan",
        "Bridge (LPBF)",
        "Cantilever (LPBF)",
        "Double-cantilever (LPBF)",
        "Coming soon",
      ]);
      await expect(slots.nth(7).locator(".rsh-animation-placeholder")).toHaveCount(1);
      if (theme === "light") await expect(page.locator("body")).toHaveCSS("background-color", "rgb(255, 255, 255)");
      const names = ["point", "single-track", "thin-wall", "scan", "bridge", "cantilever", "double-cantilever"];
      for (let i = 0; i < names.length; i++) {
        const animation = animations.nth(i);
        await expect(animation).toHaveAttribute("src", new RegExp(`${names[i]}-animation\\.webp(?:\\?v=[a-f0-9]+)?$`));
        await animation.scrollIntoViewIfNeeded();
        await expect.poll(() => animation.evaluate((image) => image.complete && image.naturalWidth > 0)).toBe(true);
        const firstFrame = await animation.screenshot();
        await expect.poll(async () => !(await animation.screenshot()).equals(firstFrame), { timeout: 10000 }).toBe(true);
      }
      await page.emulateMedia({ reducedMotion: "reduce" });
      for (let i = 0; i < names.length; i++) {
        await expect
          .poll(() => animations.nth(i).evaluate((image) => image.currentSrc))
          .toMatch(new RegExp(`${names[i]}-animation-poster\\.png(?:\\?v=[a-f0-9]+)?$`));
      }
      await expect(page.locator(".rsh-gallery button")).toHaveCount(0);
      await expect(page.locator(".rsh-welcome")).toContainText("Howdy! Welcome to Residual Stress Hub.");
    });

    test("Methods explains the reference, optimization loop, and component handoff", async ({ page }) => {
      await openPage(page, "/methods/");
      const guide = page.locator(".rsh:not(.rsh-page-brand)");
      await expect(guide.locator("pre code").first()).toHaveCSS("font-size", "13px");
      await expect(guide.locator("pre code").first()).toHaveCSS("line-height", "19.5px");
      const inlineCode = guide.locator("p code").first();
      expect(await inlineCode.evaluate((el) => parseFloat(getComputedStyle(el).fontSize))).toBeLessThan(14);
      await expect(page.locator(".rsh-guide-section h2")).toHaveText([
        "Full thermal-mechanical analysis",
        "Optimization-based inherent strain analysis",
      ]);
      await expect(page.locator(".rsh-guide-section")).toHaveCount(2);
      for (const section of await page.locator(".rsh-guide-section").all()) {
        await expect(section.locator(":scope > h3")).toHaveText([
          "Model and weak forms",
          "Element activation",
          "Solution procedure",
          "Cutting and stress release",
          "Implementation and results",
        ]);
      }
      await expect(guide.locator(".rsh-equation")).toHaveCount(4);
      await expect(guide).toContainText("inherited stress and plastic state");
      await expect(guide).toContainText("python opt_solver/run.py bridge --dry-run");
      await expect(guide).toContainText("Reset displacement, stress, and plastic history to zero.");
      await expect(guide).toContainText("inherent_strain.default");
      await expect(guide).toContainText("workflow_result.json");
      await expect(guide).not.toContainText(/Macro|Use this checklist/);
      await guide.locator('a[href="#inside-the-optimization"]').click();
      await expect(page).toHaveURL(/#inside-the-optimization$/);
      await expect(guide.locator("mjx-container").first()).toBeVisible();
      for (const details of await guide.locator("details").all()) {
        if (!(await details.evaluate((element) => element.open))) await details.locator(":scope > summary").click();
        await expect(details).toHaveAttribute("open", "");
      }
      await page.evaluate(async () => {
        if (window.MathJax?.startup?.promise) await window.MathJax.startup.promise;
      });
      await expect(guide.locator("mjx-merror, [data-mjx-error]")).toHaveCount(0);
      await expect(guide.locator(".rsh-equation mjx-container")).toHaveCount(4);
      await expect(guide.locator(".rsh-equation mjx-mtable")).toHaveCount(0);
      for (const equation of await guide.locator(".rsh-equation").all()) {
        await expect(equation).toHaveCSS("overflow-x", "auto");
        const box = await equation.boundingBox();
        expect(box.x).toBeGreaterThanOrEqual(0);
        expect(box.x + box.width).toBeLessThanOrEqual(page.viewportSize().width + 1);
      }
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBe(true);
    });

    test("Benchmarks opens Cantilever directly with paper sections, full parameters, figures and a source footer", async ({ page, request }) => {
      await openPage(page, "/benchmarks/");
      await page.locator('.rsh-card h2 a[href="/benchmarks/cantilever/"]').click();
      await expect(page).toHaveURL(/\/benchmarks\/cantilever\/$/);
      await expect(page.locator(".post > article > h2")).toHaveText(["Overview", "Problem set", "Results"]);
      await expect(page.locator("#overview")).toHaveCSS("color", theme === "light" ? "rgb(23, 25, 27)" : "rgb(245, 245, 239)");
      expect(Number(await page.locator("#overview").evaluate((heading) => getComputedStyle(heading).fontWeight))).toBeGreaterThanOrEqual(700);
      await expect(page.locator(".post > article > table")).toHaveCount(2);
      const parameters = page.locator("details.rsh-parameter-details");
      await expect(parameters).toHaveCount(1);
      await expect(parameters).not.toHaveAttribute("open", "");
      await expect(parameters.locator("table")).toHaveCount(4);
      const jsonResponse = await request.get("/assets/data/cases/cantilever/thermal-parameters.json");
      expect(jsonResponse.ok()).toBe(true);
      const data = await jsonResponse.json();
      expect(data.materials.upper_region.heat_capacity.temperature_k).toHaveLength(14);
      expect(data.materials.upper_region.conductivity.temperature_k).toHaveLength(9);
      expect(data.materials.upper_region.thermal_expansion.temperature_k).toHaveLength(8);
      expect(data.materials.upper_region.yield_stress.temperature_k).toHaveLength(4);
      await parameters.locator("summary").click();
      await expect(parameters).toHaveAttribute("open", "");
      for (const table of await parameters.locator("table").all()) await expect(table).toBeVisible();
      await expect(parameters.locator("table").nth(1).locator("tbody tr")).toHaveCount(9);
      await expect(parameters.locator("table").nth(2).locator("tbody tr")).toHaveCount(14);
      await expect(parameters.locator("table").nth(3).locator("tbody tr")).toHaveCount(4);
      await expect(parameters).toContainText("1335.85");
      await expect(parameters).toContainText("286000");
      const csvResponse = await request.get("/assets/data/cases/cantilever/temperature-dependent-properties.csv");
      expect(csvResponse.ok()).toBe(true);
      const records = (await csvResponse.text()).trim().split(/\r?\n/);
      expect(records).toHaveLength(62);
      expect(records[0]).toBe("property,temperature_k,temperature_c,value,unit,status");
      expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(await page.evaluate(() => window.innerWidth + 1));
      await parameters.locator("summary").click();
      await expect(parameters.locator("table").first()).toBeHidden();
      await expect(page.locator(".rsh-case-figures img")).toHaveCount(9);
      await expect(page.locator(".post > article")).toContainText("Reference:");
      await expect(page.locator("#reference-1")).toHaveCount(1);
      await expect(page.locator("#reference-2")).toHaveCount(1);
      await expect(page.locator("#overview + p")).toContainText("neutron diffraction and the contour method");
      await expect(page.locator('.post > article a[href="https://doi.org/10.1007/s40192-019-00149-0"]')).toBeVisible();
      await expect(page.locator('.post > article a[href="/benchmarks/"]')).toBeVisible();
    });

    for (const [slug, folder, power] of [
      ["single-track", "single_track", 600],
      ["thin-wall", "thin-wall", 2245],
      ["bridge", "bridge", 100],
      ["double-cantilever", "double_cantilever", 285],
    ]) {
      test(`${slug} provides complete expandable parameters and result downloads`, async ({ page, request }) => {
        await openPage(page, `/benchmarks/${slug}/`);
        const article = page.locator(".post > article");
        await expect(article.locator(":scope > h2")).toHaveText(["Overview", "Problem set", "Results"]);
        await expect(article.locator(":scope > h3").filter({ hasText: /^(Printing|Simulation) parameters$/ })).toHaveCount(2);
        await expect(article.locator(":scope > table")).toHaveCount(2);
        const parameters = article.locator("details.rsh-parameter-details");
        await expect(parameters).not.toHaveAttribute("open", "");
        await expect(parameters.locator("table").first()).toBeHidden();

        const response = await request.get(`/assets/data/cases/${folder}/thermal-parameters.json`);
        expect(response.ok()).toBe(true);
        const data = await response.json();
        expect(data.heat_source.power_w).toBe(power);
        expect(JSON.stringify(data)).not.toContain("/Users/");
        const expectedRows = Object.values(data.materials).reduce(
          (sum, material) => sum + Object.values(material).reduce((count, property) => count + (property?.temperature_k?.length || 0), 0),
          0
        );
        const csvResponse = await request.get(`/assets/data/cases/${folder}/temperature-dependent-properties.csv`);
        expect(csvResponse.ok()).toBe(true);
        const records = (await csvResponse.text()).trim().split(/\r?\n/);
        expect(records).toHaveLength(expectedRows + 1);
        expect(records[0]).toBe("region,material,property,temperature_k,temperature_c,value,unit,status");

        await parameters.locator("summary").click();
        await expect(parameters).toHaveAttribute("open", "");
        for (const table of await parameters.locator("table").all()) await expect(table).toBeVisible();
        expect(await parameters.locator("table").count()).toBeGreaterThan(7);
        expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(await page.evaluate(() => window.innerWidth + 1));
        await parameters.locator("summary").click();
        await expect(parameters.locator("table").first()).toBeHidden();

        const downloads = await article.locator('a[href^="/assets/"]').evaluateAll((links) => links.map((link) => link.getAttribute("href")));
        expect(downloads.some((url) => url.endsWith("simulation-parameters.yaml"))).toBe(true);
        for (const url of new Set(downloads)) expect((await request.get(url)).ok(), url).toBe(true);
        await expect(article).toContainText("Reference:");
        await expect(article.locator("#reference-1")).toHaveCount(1);
        if (["bridge", "double_cantilever"].includes(folder)) {
          const identification = await (await request.get(`/assets/data/cases/${folder}/identification-results.json`)).json();
          expect(identification.latest.inherent_strain.zz).not.toBe(identification.displayed_comparison.inherent_strain.zz);
          await expect(article).not.toContainText("Inherent strain in the displayed archived comparison");
          const strainRows = article.locator(":scope > table tbody tr").filter({ hasText: "Identified inherent strain," });
          await expect(strainRows).toHaveCount(2);
          const displayedZ = (await strainRows.last().locator("td").nth(1).innerText()).replace("−", "-");
          expect(Number(displayedZ)).toBe(Number((identification.latest.inherent_strain.zz * 1000).toFixed(3)));
          if (folder === "double_cantilever") {
            expect(data.materials.upper_region.name).toBe("IN718");
            expect(identification.latest.inherent_strain.zz).toBe(0.019647141658521924);
            expect(identification.displayed_comparison.inherent_strain.zz).toBe(0.015520309717393634);
          }
        } else {
          await expect(article).toContainText("Not used — this case uses full thermal–mechanical analysis");
        }
      });
    }

    test("old Example 1 URL renders the same Cantilever without an intermediate page", async ({ page }) => {
      await openPage(page, "/benchmarks/cantilever/");
      const content = (await page.locator(".post > article").innerText()).replace(/\s+/g, " ").trim();
      await openPage(page, "/benchmarks/example-1/");
      await expect(page).toHaveURL(/\/benchmarks\/example-1\/$/);
      await expect(page.locator(".post h1")).toHaveText("Cantilever (LPBF · IN625)");
      expect((await page.locator(".post > article").innerText()).replace(/\s+/g, " ").trim()).toBe(content);
    });

    test("old projects URL shows the list without an intermediate page", async ({ page }) => {
      await openPage(page, "/benchmarks/");
      await expect(page.locator(".rsh-card h2 a")).toHaveText([
        "Single track (DED · IN718 / Ti-6Al-4V)",
        "Thin-wall (WAAM · S355)",
        "Bridge (LPBF · Ti-6Al-4V)",
        "Cantilever (LPBF · IN625)",
        "Double-cantilever (LPBF · IN718)",
      ]);
      const cards = page.locator(".rsh-benchmark-card");
      expect((await cards.allTextContents()).map((text) => text.trim())).toEqual([
        "Single track (DED · IN718 / Ti-6Al-4V)",
        "Thin-wall (WAAM · S355)",
        "Bridge (LPBF · Ti-6Al-4V)",
        "Cantilever (LPBF · IN625)",
        "Double-cantilever (LPBF · IN718)",
      ]);
      expect(await cards.locator("img").evaluateAll((images) => images.map((image) => image.getAttribute("src").split("?")[0]))).toEqual([
        "/assets/img/cases/single_track/card-cover.png",
        "/assets/img/cases/thin-wall/card-cover.png",
        "/assets/img/cases/bridge/card-cover.png",
        "/assets/img/cases/cantilever/card-cover.png",
        "/assets/img/cases/double_cantilever/card-cover.png",
      ]);
      await expect(cards.first().locator("img")).toHaveAttribute("src", /card-cover\.png\?v=[a-f0-9]{12}$/);
      const list = (await page.locator(".rsh:not(.rsh-page-brand)").innerText()).replace(/\s+/g, " ").trim();
      await openPage(page, "/projects/");
      await expect(page).toHaveURL(/\/projects\/$/);
      expect((await page.locator(".rsh:not(.rsh-page-brand)").innerText()).replace(/\s+/g, " ").trim()).toBe(list);
      await expect(page.locator('.rsh-card h2 a[href="/benchmarks/cantilever/"]')).toBeVisible();
    });
  });
}
