# Fener Simulator

Eine Fußball-Simulations-App nur für Fenerbahçe-Spiele. Sie besteht aus einer einzigen Web-Seite und läuft im Browser, auch auf dem iPhone.

## Funktionen
- Gegner wählen: alle Süper-Lig-Teams oder europäische Topklubs
- Heim (Kadıköy), auswärts oder auf neutralem Platz
- Form von Fenerbahçe einstellen
- K.-o.-Modus mit Elfmeterschießen
- Liveticker mit Toren, Vorlagen, Karten, Wechseln, Momentum und Statistik (inklusive xG)
- Kader im Tab „Kader“ bearbeiten
- Verlauf mit Bilanz (wird auf dem Gerät gespeichert)

## Aufs iPhone
1. `index.html` irgendwo hosten, z. B. mit GitHub Pages (Settings → Pages → Branch wählen).
2. Die Seite in Safari öffnen → Teilen → „Zum Home-Bildschirm“.

## Entwicklung
Den Code in `src/app.html` bearbeiten, dann `python3 build.py` ausführen. Das erzeugt `index.html`.
