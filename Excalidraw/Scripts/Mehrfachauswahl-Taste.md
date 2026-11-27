/*
# Mehrfachauswahl-Taste / Multi-select key

**EN:** Shows an on-screen button that simulates the Shift key, so you can select several elements by
tapping. Run the script again to remove the button.

**DE:** Blendet eine Bildschirm-Taste ein, die die Umschalttaste simuliert (Mehrfachauswahl per
Antippen). Das Skript erneut starten entfernt die Taste.

Created with AI assistance / Mit KI-Unterstützung erstellt.
License / Lizenz: AGPL-3.0, Copyright (c) 2026 zniehna. Full text / Volltext:
https://github.com/zniehna/excalidraw-android-tools/blob/main/LICENSE
Provided "as is", without warranty / Ohne Gewähr.

```javascript
*/
const de = String(ea.obsidian.moment.locale()).startsWith("de");
const tx = de
  ? { noView: "Keine Excalidraw-Ansicht aktiv.", removed: "Mehrfachauswahl-Taste entfernt",
      shown: "Mehrfachauswahl-Taste eingeblendet", on: "⇧ Mehrfach: AN", off: "⇧ Mehrfach: AUS", error: "Fehler: " }
  : { noView: "No active Excalidraw view.", removed: "Multi-select key removed",
      shown: "Multi-select key shown", on: "⇧ Multi: ON", off: "⇧ Multi: OFF", error: "Error: " };
try {
  ea.setView("active");
  const view = ea.targetView;
  if (!view) { new Notice(tx.noView); return; }

  const root = view.contentEl;
  const doc = root.ownerDocument;
  const win = doc.defaultView;

  // Second run: remove button and listeners / Erneuter Start: Taste und Listener entfernen
  const old = root.querySelector(".ea-shift-toggle");
  if (old) {
    old._cleanup();
    old.remove();
    new Notice(tx.removed);
    return;
  }

  let active = false;
  let dragging = false;

  const btn = doc.createElement("button");
  btn.className = "ea-shift-toggle";
  Object.assign(btn.style, {
    position: "absolute",
    right: "12px",
    bottom: "80px",
    zIndex: "1000",
    padding: "14px 18px",
    fontSize: "16px",
    borderRadius: "12px",
    border: "2px solid var(--background-modifier-border)",
    touchAction: "manipulation",
  });
  const render = () => {
    btn.textContent = active ? tx.on : tx.off;
    btn.style.background = active ? "var(--interactive-accent)" : "var(--background-secondary)";
    btn.style.color = active ? "var(--text-on-accent)" : "var(--text-normal)";
  };
  btn.addEventListener("click", () => { active = !active; render(); });
  render();

  if (win.getComputedStyle(root).position === "static") root.style.position = "relative";
  root.appendChild(btn);

  const types = ["pointerdown", "pointermove", "pointerup", "pointercancel",
                 "mousedown", "mousemove", "mouseup", "click"];

  const patch = (e) => {
    if (!active) return;
    const t = e.target;
    if (btn.contains(t)) return;
    const onCanvas = t instanceof win.HTMLCanvasElement && root.contains(t);
    if (e.type === "pointerdown" && onCanvas) dragging = true;
    if (onCanvas || dragging) {
      try { Object.defineProperty(e, "shiftKey", { value: true, configurable: true }); } catch (_) {}
    }
    if (e.type === "pointerup" || e.type === "pointercancel") dragging = false;
  };

  types.forEach(t => win.addEventListener(t, patch, true));
  btn._cleanup = () => types.forEach(t => win.removeEventListener(t, patch, true));

  new Notice(tx.shown);
} catch (err) {
  new Notice(tx.error + (err && err.message ? err.message : err), 15000);
}
