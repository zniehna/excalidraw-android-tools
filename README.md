# excalidraw-android-tools

🌐 Language: **English** | [Deutsch](README.de.md)

Two scripts for the [Excalidraw plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin) in
Obsidian on an Android tablet.

| Script | What it does | Guide |
|---|---|---|
| **Slideshow Mobil PDF** | The Slideshow script with PDF export on mobile and fixes for the tablet display | [guide](docs/slideshow-mobile-pdf.md) |
| **Mehrfachauswahl-Taste** (multi-select key) | On-screen key that acts like Shift, to select several elements by tapping | [guide](docs/multi-select-key.md) |

## Installation

1. For each script you want, copy the `.md` file **and** the `.svg` file with the same name from
   `Excalidraw/Scripts/` into the script folder of your vault. The default used here is
   `Excalidraw/Scripts/`; check the script folder in the Excalidraw plugin settings.
2. Put the files directly into that folder, not into `Downloaded/`. In our test with another script,
   its own icon was not shown in `Downloaded/`.
3. Restart Obsidian. Start a script with the command `(Script) <file name>` or from the Excalidraw
   tools panel. Do not rename the files: the name defines the command, the icon and the stored settings.

## Created with AI assistance

The code, the icon changes and the documentation in this repository were created **with the help of
AI**. Slideshow Mobil PDF builds on the original code by Zsolt Viczian. The scripts are tested only
as far as stated in the guides. Use them at your own risk.

## License

**AGPL-3.0**: free to use, change and share. If you pass on a changed version, it must also be
under the AGPL-3.0, with source code and the existing copyright notices.
Details: [LICENSING.md](LICENSING.md).

This project is not affiliated with or endorsed by Zsolt Viczian, Obsidian or Excalidraw.
