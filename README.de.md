# excalidraw-android-tools

🌐 Sprache: [English](README.md) | **Deutsch**

Zwei Skripte für das [Excalidraw-Plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin) in
Obsidian auf einem Android-Tablet.

| Skript | Zweck | Anleitung |
|---|---|---|
| **Slideshow Mobil PDF** | Das Slideshow-Skript mit PDF-Export auf Mobilgeräten und Korrekturen für die Anzeige auf dem Tablet | [Anleitung](docs/slideshow-mobile-pdf.de.md) |
| **Mehrfachauswahl-Taste** | Bildschirmtaste, die wie die Umschalttaste wirkt, um mehrere Elemente durch Antippen auszuwählen | [Anleitung](docs/multi-select-key.de.md) |

## Installation

1. Kopiere für jedes gewünschte Skript die `.md`-Datei **und** die gleichnamige `.svg`-Datei aus
   `Excalidraw/Scripts/` in den Skriptordner deines Vaults. Hier wird `Excalidraw/Scripts/`
   verwendet. Maßgeblich ist der in den Einstellungen des Excalidraw-Plugins eingetragene Ordner.
2. Lege die Dateien direkt in diesen Ordner, nicht in `Downloaded/`. In unserem Test mit einem
   anderen Skript wurde dessen eigenes Icon in `Downloaded/` nicht angezeigt.
3. Starte Obsidian neu. Ein Skript startest du mit dem Befehl `(Script) <Dateiname>` oder über das
   Werkzeug-Panel von Excalidraw. Benenne die Dateien nicht um: Der Name bestimmt Befehl, Icon und
   gespeicherte Einstellungen.

## Mit KI-Unterstützung erstellt

Der Code, die Änderungen am Icon und die Dokumentation in diesem Repository wurden **mit
Unterstützung von KI** erstellt. Slideshow Mobil PDF baut auf dem Originalcode von Zsolt Viczian auf.
Getestet sind die Skripte nur so weit, wie in den Anleitungen angegeben. Nutzung auf eigene Gefahr.

## Lizenz

**AGPL-3.0**: freie Nutzung, Änderung und Weitergabe. Wer eine geänderte Fassung weitergibt, muss
sie ebenfalls unter die AGPL-3.0 stellen, mit Quellcode und den vorhandenen Urhebervermerken.
Einzelheiten: [LICENSING.md](LICENSING.md).

Dieses Projekt ist nicht mit Zsolt Viczian, Obsidian oder Excalidraw abgestimmt oder verbunden.
