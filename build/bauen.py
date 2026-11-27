#!/usr/bin/env python3
"""Builds "Slideshow Mobil PDF.md" from the original Slideshow script.

Baut "Slideshow Mobil PDF.md" aus dem originalen Slideshow-Skript.

Usage / Aufruf:
  python3 build/bauen.py                 download the original / Original herunterladen
  python3 build/bauen.py Slideshow.md    use a local copy / lokale Kopie verwenden
"""
import hashlib
import sys
import urllib.request
from pathlib import Path

COMMIT = "cd667faacfa1f1cff8cd101d9d117e31c51397b2"
SHA256 = "9e6e8b2f7cd6f96412a75d62ffc1452591ad80f15f9c26dd030664fd2968b114"
URL = f"https://raw.githubusercontent.com/zsviczian/obsidian-excalidraw-plugin/{COMMIT}/ea-scripts/Slideshow.md"

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent / "Excalidraw" / "Scripts" / "Slideshow Mobil PDF.md"


def read(path):
    return path.read_bytes().decode("utf-8")


def patches():
    """List of (description, original text, new text). Each original text must occur exactly once."""
    css = ".slideshow-sidepanel__header .slideshow-sidepanel__icon-button { width:36px; height:36px; min-width:36px; padding:7px; }\n"
    modal_title = '      modal.titleEl.setText(t("printDialogTitle"));\n'
    generate = "  async function generateSlideshowPdf(options, settings) {\n"
    create_pdf = "      await ea2.createPDF({\n        SVG: selectedPages,\n"
    buttons_old = """      const error = modal.contentEl.createEl("p", { cls: "mod-warning", attr: { role: "alert" } });
      const actions = modal.contentEl.createDiv({ cls: "modal-button-container" });
"""
    buttons_new = """      const footer = modal.contentEl.createDiv();
      footer.setCssStyles({
        position: "sticky",
        bottom: "0",
        zIndex: "10",
        paddingBottom: "4px",
        backgroundColor: "var(--modal-background, var(--background-primary))"
      });
      const error = footer.createEl("p", { cls: "mod-warning", attr: { role: "alert" } });
      error.setCssStyles({ margin: "0" });
      const actions = footer.createDiv({ cls: "modal-button-container" });
"""
    return [
        ("header", "/*\n# Slideshow\n", "/*\n" + read(HERE / "header.md") + "# Slideshow\n"),
        ("side panel title", '    sidepanelTitle: "Slideshow",\n', '    sidepanelTitle: "Slideshow Mobil PDF",\n'),
        ("icon-only buttons", css, css
         + ".slideshow-sidepanel button:has(> svg:only-child) { display:inline-flex; align-items:center; justify-content:center; padding:0 !important; }\n"
         + ".slideshow-sidepanel button > svg:only-child { flex:0 0 auto; width:18px; height:18px; }\n"),
        ("dialog scrolling", modal_title, modal_title
         + "      // FloatingModal treats touches as dragging and blocks scrolling while doing so.\n"
         + '      for (const type of ["touchstart", "pointerdown"])\n'
         + "        modal.contentEl.addEventListener(type, (event) => event.stopPropagation(), { passive: true });\n"),
        ("sticky buttons", buttons_old, buttons_new),
        ("mobile print functions", generate, read(HERE / "mobile_print.js") + generate),
        ("use mobile print", create_pdf,
         "      if (ea2.DEVICE.isMobile) {\n"
         '        await printSlidesMobile(selectedPages, settings, pageBackground, targetFile?.basename ?? "slideshow");\n'
         "        return;\n"
         "      }\n" + create_pdf),
        ("runtime name", '"__excalidrawAutomateSlideshowRuntimeV1"', '"__excalidrawAutomateSlideshowMobilPdfRuntimeV1"'),
    ]


def main():
    if len(sys.argv) > 1:
        data = Path(sys.argv[1]).read_bytes()
    else:
        with urllib.request.urlopen(URL, timeout=60) as response:
            data = response.read()
    if hashlib.sha256(data).hexdigest() != SHA256:
        sys.exit("Checksum mismatch: this is not the expected original. / Falscher Originalstand.")
    text = data.decode("utf-8")
    for name, old, new in patches():
        if text.count(old) != 1:
            sys.exit(f"Patch '{name}': expected exactly one match, found {text.count(old)}.")
        text = text.replace(old, new)
    TARGET.write_bytes(text.encode("utf-8"))
    print(f"Written / Geschrieben: {TARGET}")


if __name__ == "__main__":
    main()
