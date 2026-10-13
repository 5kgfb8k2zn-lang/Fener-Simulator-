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
- **Mit API-Key**: Echter Stand (Tabelle, Ergebnisse, Termine) wird automatisch geladen, höchstens alle 6 Stunden. Die echte Aufstellung lässt sich als Startelf übernehmen.

## Simulation: so realistisch wie möglich
- Die Engine ist auf Süper-Lig-Durchschnittswerte abgestimmt: ca. 2,8 Tore pro Spiel, 12 Schüsse und 5 Ecken pro Team, 34 % aufs Tor, 2,2 Gelbe und 0,13 Platzverweise pro Team, Heimbilanz ca. 44/26/30.
- Formfaktor: Die Stärkewerte werden anhand der echten Tordifferenz pro Spiel nachjustiert (Gewicht wächst mit der Zahl der Spiele, höchstens ±6).
- Sperren: Liga nach jeder 4. Gelben, CL und Pokal nach jeder 3., Gelb-Rot 1 Spiel, Rot 2 Spiele, jeweils im selben Wettbewerb. Verletzungen dauern 1 bis 17 Spiele. Ausfälle werden positionsgerecht von der Bank ersetzt.
- Live-Spiele: Taktik umstellen und selbst wechseln, auf Wunsch ohne automatische Wechsel.

## Aufs iPhone
1. `index.html` irgendwo hosten, z. B. mit GitHub Pages (Settings → Pages → Branch wählen).
2. Die Seite in Safari öffnen → Teilen → „Zum Home-Bildschirm“.

## Entwicklung
Den Code in `src/app.html` bearbeiten, dann `python3 build.py` ausführen. Das erzeugt `index.html`.

## Datenstand
Kader, Tabelle und Spielplan entsprechen dem Stand vom 13.10.2026. Annahmen: Die Rückrunde ist die gespiegelte Hinrunde mit geschätzten Terminen. Bei einigen Teams ist die Tordifferenz geschätzt. K.-o.-Gegner in der CL und im Pokal werden zufällig gelost. Die Stärkewerte der Teams sind Einschätzungen.

## Echter Live-Ticker
Der Tab „Live“ zeigt echte Spielstände von Fenerbahçe, der Süper Lig, der Champions League und des Pokals. Die Daten kommen von [API-Football](https://www.api-football.com/).
1. Die App über GitHub Pages öffnen. In der Claude-Vorschau sind Verbindungen zu fremden Diensten gesperrt.
2. Kostenlos auf dashboard.api-football.com registrieren und den API-Key kopieren.
3. Den Key im Tab „Live“ einfügen. Er wird nur im Browser gespeichert und nie ins Repository geschrieben.

**Abfragen nach Spielplan:** Die App fragt nur rund um Fener-Spiele ab. Im Standard „Maximal“ nutzt sie am Spieltag das ganze Tageslimit (etwa alle 70 Sekunden, Tore im Schnitt ca. 1 Minute später). Nach Abpfiff trägt sie das Ergebnis automatisch in die Saison ein. Abgefragt wird von 5 Minuten vor Anpfiff bis Abpfiff, in der Halbzeit seltener. Im Test brauchte ein ganzer Spieltag etwa 50 Anfragen, an anderen Tagen braucht die App höchstens 2. Es gibt einen Zähler pro Tag, 5 Anfragen bleiben immer als Reserve, und die App drosselt sich selbst, wenn das Budget knapp wird. Nach Abpfiff lässt sich das echte Ergebnis mit einem Tipp in die Saison-Simulation übernehmen.

## Hintergrund-Helfer (Push bei geschlossener App)
Im Ordner `helfer/` liegt ein Cloudflare Worker. Er fragt API-Football rund um Fener-Spiele etwa jede Minute ab und schickt über die App ntfy Push-Nachrichten bei Anpfiff, Toren, Roten Karten, Halbzeit und Abpfiff. Ist der Helfer in der App eingetragen, holt die App alles von ihm und verbraucht selbst keine Anfragen mehr. Die Einrichtung steht Schritt für Schritt in `helfer/ANLEITUNG.md`. In der App lässt sich einstellen, welche Nachrichten kommen sollen, und eine Grafik zeigt den Verlauf der Siegchance.
