# Fener Simulator

Eine Fußball-Simulations-App nur für Fenerbahçe-Spiele. Sie besteht aus einer einzigen Web-Seite und läuft im Browser, auch auf dem iPhone.

## Funktionen
- **Zwei Saison-Modi**: „Aktueller Stand“ (echte Tabelle und Ergebnisse) oder „Ab 1. Spieltag“ (alle Teams bei 0, ganze Saison selbst simulieren).
- **Saison 2026/27**: startet beim echten Stand vom 13.10.2026 (Tabelle nach dem 7. Spieltag, Fener-Ergebnisse, Champions-League-Auslosung). Spiel für Spiel live oder als Ergebnis simulieren, oder den Rest der Saison auf einmal. Die Tabelle läuft mit, inklusive Champions-League-K.-o.-Runde und Türkiye Kupası.
- Einzelspiel gegen jeden Süper-Lig-Klub 2026/27 oder europäische Topklubs
- Heim (Kadıköy), auswärts oder auf neutralem Platz
- Form von Fenerbahçe einstellen
- K.-o.-Modus mit Elfmeterschießen
- Liveticker mit Toren, Vorlagen, Karten, Wechseln, Momentum und Statistik (inklusive xG)
- Kader im Tab „Kader“ bearbeiten
- Verlauf mit Bilanz (wird auf dem Gerät gespeichert)

## Weitere Funktionen
- **Prognose fürs nächste Spiel**: 1000 Simulationen ergeben die Wahrscheinlichkeiten für Sieg, Remis und Niederlage und das wahrscheinlichste Ergebnis.
- **Saison-Prognose**: 300 komplette Durchläufe ergeben die Chancen auf Meisterschaft, CL-Runden und Pokal.
- **Kader**: Spielerstärken, Teamstärke, Spieler tauschen, Ausrichtung defensiv/ausgewogen/offensiv.
- **Konferenz**: Bei live gespielten Ligaspielen laufen die anderen Spiele des Spieltags mit.
- **Derby-Modus** gegen Galatasaray, Beşiktaş und Trabzonspor mit eigenen Kommentaren und mehr Karten.
- **Torjubel mit Ton**, Verletzungen, Spielerstatistik der Saison (Tore, Vorlagen, Spieler des Spiels).
- **Echte Ergebnisse von Hand eintragen**: Offenes Spiel im Spielplan antippen.
- **Tippspiel** für die nächsten echten Fener-Spiele.

## Simulation: so realistisch wie möglich
- Die Engine ist auf Süper-Lig-Durchschnittswerte abgestimmt: ca. 2,8 Tore pro Spiel, 12 Schüsse und 5 Ecken pro Team, 34 % aufs Tor, 2,2 Gelbe und 0,13 Platzverweise pro Team, Heimbilanz ca. 44/26/30.
- Formfaktor: Die Stärkewerte werden anhand der echten Tordifferenz pro Spiel nachjustiert (Gewicht wächst mit der Zahl der Spiele, höchstens ±6).
- Sperren: Liga nach jeder 4. Gelben, CL und Pokal nach jeder 3., Gelb-Rot 1 Spiel, Rot 2 Spiele, jeweils im selben Wettbewerb. Verletzungen dauern 1 bis 17 Spiele. Ausfälle werden positionsgerecht von der Bank ersetzt.
- Live-Spiele laufen komplett automatisch, der Trainer wechselt selbst.
- Spielverlauf: Wer zurückliegt, drängt (stärker gegen Ende), wer führt, verwaltet. Ca. 45 % der Tore fallen vor der Pause, gut 20 % ab der 76. Minute. Dazu Elfmeter (ca. 0,3 pro Spiel), Eigentore, Torwart-Qualität, Nachspielzeit von 1–5 bzw. 3–8 Minuten.
- Heimvorteil je Stadion (Kadıköy, RAMS Park, Papara Park etwas stärker), Englische Wochen machen müde.
- Saisonwerte im Test: Meister ca. 81 Punkte aus 34 Spielen, Platz 16 ca. 29.

## Aufs iPhone
1. `index.html` irgendwo hosten, z. B. mit GitHub Pages (Settings → Pages → Branch wählen).
2. Die Seite in Safari öffnen → Teilen → „Zum Home-Bildschirm“.

## Entwicklung
Den Code in `src/app.html` bearbeiten, dann `python3 build.py` ausführen. Das erzeugt `index.html`.

## Datenstand
Kader, Tabelle und Spielplan entsprechen dem Stand vom 13.10.2026. Annahmen: Die Rückrunde ist die gespiegelte Hinrunde mit geschätzten Terminen. Bei einigen Teams ist die Tordifferenz geschätzt. K.-o.-Gegner in der CL und im Pokal werden zufällig gelost. Die Stärkewerte der Teams sind Einschätzungen.

## Echter Live-Ticker
Der Tab „Live“ zeigt echte Spielstände von Fenerbahçe, Ergebnisse, Tabelle und Rivalen. Die Daten holt der Hintergrund-Helfer (siehe unten) kostenlos von TheSportsDB. Für Echtzeit gibt es Knöpfe zu Google und Sofascore. Nach Abpfiff wird das echte Ergebnis automatisch in die Saison eingetragen.

## Hintergrund-Helfer (Push bei geschlossener App)
Im Ordner `helfer/` liegt ein Cloudflare Worker. Er holt die Fener-Spiele kostenlos von TheSportsDB und schickt über die App ntfy Push-Nachrichten bei Anpfiff, Toren, Halbzeit und Endergebnis, dazu eine Erinnerung am Spieltag und die Rivalen-Ergebnisse. Die Einrichtung steht Schritt für Schritt in `helfer/ANLEITUNG.md`. In der App lässt sich einstellen, welche Nachrichten kommen sollen, und eine Grafik zeigt den Verlauf der Siegchance.

## Datenquelle des Helfers
**TheSportsDB** (kostenlos, für private Projekte erlaubt, kein Schlüssel): Spielplan, Ergebnisse, Tabelle, Rivalen. Während eines Fener-Spiels fragt der Helfer jede Minute nach dem Spielstand, danach bis zum Endergebnis. Spielstände können verzögert sein, weil TheSportsDB sie selbst erst einträgt.
