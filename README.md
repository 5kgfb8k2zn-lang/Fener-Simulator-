# Fener Simulator

Eine Fußball-Simulations-App nur für Fenerbahçe-Spiele. Sie besteht aus einer einzigen Web-Seite und läuft im Browser, auch auf dem iPhone.

## Funktionen
- **Saison 2026/27**: startet beim echten Stand vom 13.10.2026 (Tabelle nach dem 7. Spieltag, Fener-Ergebnisse, Champions-League-Auslosung). Spiel für Spiel live oder als Ergebnis simulieren, oder den Rest der Saison auf einmal. Die Tabelle läuft mit, inklusive Champions-League-K.-o.-Runde und Türkiye Kupası.
- Einzelspiel gegen jeden Süper-Lig-Klub 2026/27 oder europäische Topklubs
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

## Datenstand
Kader, Tabelle und Spielplan entsprechen dem Stand vom 13.10.2026. Annahmen: Die Rückrunde ist die gespiegelte Hinrunde mit geschätzten Terminen. Bei einigen Teams ist die Tordifferenz geschätzt. K.-o.-Gegner in der CL und im Pokal werden zufällig gelost. Die Stärkewerte der Teams sind Einschätzungen.
