# Slideshow Mobil PDF

🌐 Language: **English** | [Deutsch](slideshow-mobile-pdf.de.md)

[Back to overview](../README.md)

A modified version of the **Slideshow** script by Zsolt Viczian, created with AI assistance.
For presenting and all other functions, see the description of the original at the top of the script
file. If you like Slideshow, support its author (link in the side panel).

## What is different

- **PDF on mobile:** the original ends in `ea.createPDF`, which produced no file in our test on
  Android. On mobile, this version builds an HTML document with one page per sheet and passes it to
  the native print function of Obsidian. On desktop, `ea.createPDF` is still used.
- **Print dialog:** you can scroll by swiping inside the content. "Cancel", "Create PDF" and error
  messages stay at the bottom. Move the window by its title or edge.
- **Side panel:** icon-only buttons show their icons.
- Own name, own icon (projector with a small phone), own side panel title.

## Usage

1. Open a drawing with frames (or a line presentation) and start `(Script) Slideshow Mobil PDF`.
2. Tap the printer button in the side panel.
3. Choose your settings and tap **Create PDF**.
4. In the system print dialog, choose saving as PDF.

## Limitations

- The mobile function is **not part of the Obsidian plugin API**. An update may break it.
  The script reports an error if the function is missing (it expects Obsidian 1.15 or newer).
- The mobile print always requests **A4**, even if you choose another page size in the dialog.

## Test status

Tested on a Samsung Galaxy Tab S9 Ultra (Android 16, Obsidian 1.15.0, Excalidraw plugin 2.29.2):
the script works and its icon is displayed correctly. PDF export, scrolling in the print dialog and
the side panel icons were confirmed individually.

**Not tested:** portrait view of the dialog and moving it after the fix, handout and notes layouts,
other paper sizes, iPad and iPhone, other Android devices, desktop.

## Rebuilding

`python3 build/bauen.py` downloads the original at a fixed commit, checks its SHA-256 checksum and
applies all changes. The changes are listed in `build/bauen.py`, `build/mobile_print.js` and
`build/header.md`.

## License

AGPL-3.0, see [LICENSING.md](../LICENSING.md).
