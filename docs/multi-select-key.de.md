# Mehrfachauswahl-Taste

🌐 Sprache: [English](multi-select-key.md) | **Deutsch**

[Zurück zur Übersicht](../README.de.md)

Ohne Tastatur fehlt die Umschalttaste, die man beim Auswählen gedrückt hält. Dieses Skript blendet
dafür eine Bildschirmtaste ein.

## Bedienung

1. Öffne eine Zeichnung und starte `(Script) Mehrfachauswahl-Taste`. Unten rechts erscheint eine Taste.
2. Tippe darauf, um sie **einzuschalten**, und tippe dann die gewünschten Elemente an.
3. Tippe erneut darauf, um sie **auszuschalten**.
4. Starte das Skript noch einmal, um die Taste zu entfernen.

Die Texte sind deutsch, wenn Obsidian auf Deutsch eingestellt ist, sonst englisch.

## Funktionsweise

Solange die Taste an ist, werden Stift-, Maus- und Klick-Ereignisse auf der Zeichenfläche so
markiert, als wäre die Umschalttaste gedrückt. Das hängt vom Verhalten des Browsers und von
Excalidraw ab und kann nach einem Update ausfallen. Auch andere Umschalt-Funktionen von Excalidraw
können in dieser Zeit greifen.

## Teststand

Auf einem Samsung Galaxy Tab S9 Ultra getestet: Das Skript funktioniert, und sein Icon wird richtig
angezeigt. **Nicht getestet:** andere Geräte und Betriebssysteme.

## Lizenz

AGPL-3.0, siehe [LICENSING.md](../LICENSING.md).
