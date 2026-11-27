# Slideshow Mobil PDF

🌐 Sprache: [English](slideshow-mobile-pdf.md) | **Deutsch**

[Zurück zur Übersicht](../README.de.md)

Eine geänderte Fassung des Skripts **Slideshow** von Zsolt Viczian.
Das Präsentieren und alle weiteren Funktionen erklärt die (englische) Beschreibung des Originals am
Anfang der Skriptdatei. Wenn dir Slideshow gefällt, unterstütze den Autor (Link in der Seitenleiste).

## Was ist anders

- **PDF auf Mobilgeräten:** Das Original endet in `ea.createPDF`. In unserem Test auf Android
  entstand damit keine Datei. Diese Fassung baut auf Mobilgeräten ein HTML-Dokument mit einer Seite
  je Blatt und übergibt es an die native Druckfunktion von Obsidian. Auf dem Desktop wird weiterhin
  `ea.createPDF` verwendet.
- **Druckdialog:** Du kannst durch Wischen im Inhalt scrollen. „Cancel“, „Create PDF“ und
  Fehlermeldungen bleiben unten stehen. Das Fenster verschiebst du am Titel oder Rand.
- **Seitenleiste:** Reine Symbolknöpfe zeigen ihre Symbole an.
- Eigener Name, eigenes Icon (Beamer mit kleinem Handy), eigener Titel in der Seitenleiste.

## Bedienung

1. Öffne eine Zeichnung mit Frames (oder einer Linien-Präsentation) und starte
   `(Script) Slideshow Mobil PDF`.
2. Tippe in der Seitenleiste auf den Drucken-Knopf.
3. Wähle die Einstellungen und tippe auf **Create PDF**.
4. Wähle im Druckdialog des Systems das Speichern als PDF.

## Grenzen

- Die Mobilfunktion gehört **nicht zur Plugin-API von Obsidian**. Ein Update kann sie unbrauchbar
  machen. Fehlt die Funktion, meldet das Skript einen Fehler (erwartet Obsidian 1.15 oder neuer).
- Der Druck auf Mobilgeräten fordert immer **A4** an, auch wenn im Dialog eine andere Seitengröße
  gewählt ist.

## Teststand

Getestet auf einem Samsung Galaxy Tab S9 Ultra (Android 16, Obsidian 1.15.0, Excalidraw-Plugin
2.29.2): Das Skript funktioniert, und sein Icon wird richtig angezeigt. PDF-Export, Scrollen im
Druckdialog und die Symbole der Seitenleiste wurden einzeln bestätigt.

**Nicht getestet:** Hochformat und Verschieben des Dialogs nach der Korrektur, Handout- und
Notiz-Layouts, andere Papierformate, iPad und iPhone, andere Android-Geräte, Desktop.

## Neu bauen

`python3 build/bauen.py` lädt das Original in einem festen Stand herunter, prüft die
SHA-256-Prüfsumme und wendet alle Änderungen an. Die Änderungen stehen in `build/bauen.py`,
`build/mobile_print.js` und `build/header.md`.

## Lizenz

AGPL-3.0, siehe [LICENSING.md](../LICENSING.md).
