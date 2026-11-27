# Mehrfachauswahl-Taste (multi-select key)

🌐 Language: **English** | [Deutsch](multi-select-key.de.md)

[Back to overview](../README.md)

Without a keyboard there is no Shift key to hold while selecting. This script adds an on-screen key
that does this.

## Usage

1. Open a drawing and start `(Script) Mehrfachauswahl-Taste`. A button appears at the lower right.
2. Tap it to switch it **on**, then tap the elements you want to select.
3. Tap it again to switch it **off**.
4. Run the script again to remove the button.

The texts are German if Obsidian is set to German, otherwise English.

## How it works

While the key is on, pointer, mouse and click events on the drawing canvas are marked as if Shift
were pressed. This relies on browser and Excalidraw behavior and may stop working after an update.
Other Shift functions of Excalidraw may also take effect while the key is on.

## Test status

Tested on a Samsung Galaxy Tab S9 Ultra: the script works and its icon is displayed correctly.
**Not tested:** other devices and operating systems.

## License

AGPL-3.0, see [LICENSING.md](../LICENSING.md).
