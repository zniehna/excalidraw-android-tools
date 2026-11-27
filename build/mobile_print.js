  // --- Slideshow Mobil PDF: start ---
  // This block: Copyright (c) 2026 zniehna, created with AI assistance.
  // License: AGPL-3.0, see LICENSING.md.
  // Several SVGs in one HTML document share one ID namespace,
  // so every page gets its own IDs.
  function mobilePrefixIds(root, prefix) {
    const withId = Array.from(root.querySelectorAll("[id]"));
    if (!withId.length) return;
    const ids = new Map(withId.map((node) => [node.getAttribute("id"), prefix + node.getAttribute("id")]));
    const mapUrls = (text) => text.replace(
      /url\(\s*(["']?)#([^"')]+)\1\s*\)/g,
      (match, quote, id) => ids.has(id) ? `url(${quote}#${ids.get(id)}${quote})` : match
    );
    for (const node of [root, ...root.querySelectorAll("*")]) {
      for (const attribute of Array.from(node.attributes)) {
        const value = attribute.value;
        let next = value;
        if ((attribute.name === "href" || attribute.name === "xlink:href") && value.startsWith("#")) {
          const id = value.slice(1);
          if (ids.has(id)) next = `#${ids.get(id)}`;
        } else if (value.includes("url(")) {
          next = mapUrls(value);
        }
        if (next !== value) attribute.value = next;
      }
      if (node.localName === "style" && node.textContent.includes("url(")) {
        node.textContent = mapUrls(node.textContent);
      }
    }
    for (const node of withId) node.setAttribute("id", ids.get(node.getAttribute("id")));
  }

  function buildMobilePrintHtml(svgPages, settings, background, title) {
    const landscape = settings.width >= settings.height;
    const widthMm = landscape ? 297 : 210;
    // 1 mm less, so that rounding does not create blank pages.
    const heightMm = (landscape ? 210 : 297) - 1;
    const color = /^(#[0-9a-fA-F]{3,8}|[a-zA-Z]+|rgba?\([\d.,%\s]+\))$/.test(background ?? "") ? background : "#fff";
    const body = svgPages.map((source, index) => {
      const svg = source.cloneNode(true);
      mobilePrefixIds(svg, `p${index}-`);
      svg.setAttribute("width", "100%");
      svg.setAttribute("height", "100%");
      svg.setAttribute("preserveAspectRatio", "xMidYMid meet");
      return `<div class="page">${new XMLSerializer().serializeToString(svg)}</div>`;
    }).join("");
    const safeTitle = title.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    const css = `@page { size: A4 ${landscape ? "landscape" : "portrait"}; margin: 0; }
html, body { margin: 0; padding: 0; background: ${color}; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: ${widthMm}mm; height: ${heightMm}mm; overflow: hidden; background: ${color}; break-after: page; }
.page:last-child { break-after: auto; }
.page > svg { display: block; }`;
    return {
      landscape,
      html: `<!doctype html><html><head><meta charset="utf-8"><title>${safeTitle}</title><style>${css}</style></head><body>${body}</body></html>`
    };
  }

  // Uses the native print function of Obsidian Mobile (not part of the plugin API).
  async function printSlidesMobile(svgPages, settings, background, title) {
    try {
      const nativeApp = window.Capacitor?.Plugins?.App;
      if (typeof nativeApp?.printToPdf !== "function") {
        throw new Error("App.printToPdf is not available (requires Obsidian 1.15 or newer)");
      }
      const { html, landscape } = buildMobilePrintHtml(svgPages, settings, background, title);
      await nativeApp.printToPdf({
        title,
        html,
        baseUrl: document.baseURI,
        pageSize: "A4",
        landscape,
        marginsType: 1
      });
    } catch (error) {
      new Notice(`Slideshow Mobil PDF: ${error?.message ?? error}`, 15000);
      throw error;
    }
  }
  // --- Slideshow Mobil PDF: end ---
