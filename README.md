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
- **Prognose fürs nächste Spiel**: Sieg, Remis, Niederlage, wahrscheinlichstes Ergebnis und Erwartungstore aus dem gemeinsamen Erwartungsmodell (Dixon-Coles), dazu Moral, Kraft der Startelf und Formation.
- **Saison-Prognose**: 300 komplette Durchläufe ergeben die Chancen auf Meisterschaft, CL-Runden und Pokal.
- **Kader**: Spielerwerte (Tempo, Abschluss, Passspiel, Defensive, Physis, Ausdauer, Kraft), Mannschaftsteile Angriff/Kontrolle/Abwehr/Torwart, Formation, Spieler tauschen, Ausrichtung defensiv/ausgewogen/offensiv.
- **Konferenz**: Bei live gespielten Ligaspielen laufen die anderen Spiele des Spieltags mit.
- **Derby-Modus** gegen Galatasaray, Beşiktaş und Trabzonspor mit eigenen Kommentaren und mehr Karten.
- **Torjubel mit Ton**, Verletzungen, Spielerstatistik der Saison (Tore, Vorlagen, Spieler des Spiels).
- **Echte Ergebnisse von Hand eintragen**: Offenes Spiel im Spielplan antippen.
- **Tippspiel** für die nächsten echten Fener-Spiele.
- **Rekorde** über alle simulierten Saisons: Titel, Punkte, höchster Sieg und höchste Niederlage, Serien, Torschützen.
- **Derby-Bilanz** gegen Galatasaray, Beşiktaş und Trabzonspor über alle Saisons.
- **Spielerform:** Gute Noten machen Spieler für die nächsten Spiele stärker, schwache schwächer (sichtbar im Kader und beim nächsten Spiel).

## Simulation (Engine v2)
Kalibriert auf die Süper Lig 2022/23–2025/26 (1.342 Spiele, football-data.co.uk) und StatsBomb-Ereignisdaten.

**Teamstärke aus Spielerwerten.** Jeder Spieler hat Werte für Tempo, Abschluss, Passspiel, Defensive, Physis, Ausdauer, Laufbereitschaft, Härte, Elfmeter und (Torwart) Paraden. Daraus entstehen vier Mannschaftsteile: Angriff, Kontrolle, Abwehr und Torwart. Spieler auf fremder Position verlieren 5–30 %, müde Spieler bis zu ~12 %. Dazu kommen Teamform (echte Tordifferenz), Moral (Ergebnisse gegen die Erwartung, Derbys) und Frische (Spielminuten kosten Kraft, Ruhetage bringen sie zurück; in englischen Wochen rotiert der Trainer).

**Ein Erwartungsmodell für alles.** log λ = log 1,415 + Heimvorteil (±0,117) + 1,2·tanh(Δ/36) − Torwart-Effekt, mit Δ = 0,6·(Angriff − gegn. Abwehr) + 0,4·(Kontrolle − gegn. Kontrolle). Die Sättigung (tanh) verhindert unrealistische Kantersiege. Engine, Prognose, Saison-Hochrechnung, Hintergrundspiele, Live-Siegchance und Helfer rechnen mit derselben Formel; Prognosen nutzen Dixon-Coles (ρ = −0,11).

**Ereignisbasierte Engine (Minute für Minute).** Ballbesitzphasen, Chancen aus dem Spiel (Großchance, Schuss im Strafraum, Kopfball, Distanzschuss mit eigenem xG), Konter nach Ballgewinn, Ecken, Freistöße, Elfmeter (Schütze gegen Torwart), Abpraller und Eigentore. Ob ein Schuss reingeht, hängt vom Schützen und vom Torwart ab (Post-Shot-xG). Beide Mannschaften haben Spieler, Karten, Verletzungen, Kraft und Wechsel. Gegner haben ein Profil (tiefer Block, Pressing, Konter, Standards, Härte), z. B. tief stehende Süper-Lig-Teams, Ballbesitzteams wie Man City, Konterteams wie Real Madrid.

**Dynamik im Spiel.** Führende verwalten (weniger Schüsse, mehr Konter), Zurückliegende drängen; beide Trainer stellen die Taktik um und wechseln nach Plan (5 Wechsel, 3 Unterbrechungen plus Halbzeit) oder bei Müdigkeit, Verletzung und Platzverweis. Taktik hat echte Vor- und Nachteile: Offensiv lohnt sich als Favorit, Defensiv als Außenseiter. Nachspielzeit ergibt sich aus Toren, Wechseln, Verletzungen und Karten. K.-o.-Spiele haben Verlängerung und ein echtes Elfmeterschießen (ABAB, Schützen nach Elfmeterwert). Jedes Spiel hat einen Startwert und lässt sich exakt wiederholen; der strukturierte Match-Log steht im Ergebnis.

**Messwerte (Engine) gegen echte Daten:**

| Kennzahl | Engine | Süper Lig / Literatur |
|---|---|---|
| Tore je Spiel, gleich starke Teams | 2,6–2,9 | 2,85 |
| 0:0 / 1:1 | 7–8 % / 13 % | 7,2 % / 12,3 % |
| Schüsse / aufs Tor je Spiel | 24–25 / 8,5 | 25,3 / 8,9 |
| Gelb / Rot je Spiel | 4,5 / 0,24 | 4,55 / 0,22 |
| Derby: Tore, Gelb, Rot | 2,35 / 6,6 / 0,6 | 2,35 / 6,2–7,0 / 0,48–0,61 |
| Elfmeter je Spiel | 0,32–0,38 | 0,37–0,43 |
| Anteil Tore 1. Halbzeit | 45 % | 44 % |
| Führung 1:0 zur Pause → Sieg/Remis/Niederlage | 67/22/11 % | 66/22/12 % |
| Führung mit 2 Toren → Sieg | 89 % | 90,5 % |
| Torrate in Unterzahl | ×0,57 | ×0,61 |
| Wechsel je Team / Zeitpunkte (Median) | 4,4 / 69' | 4,3 / ~74' |
| 7+ Tore in einem Spiel (gleich stark) | 2 % | 2,6 % |

- Sperren: Liga nach jeder 4. Gelben, CL und Pokal nach jeder 3., Gelb-Rot 1 Spiel, Rot 2 Spiele, jeweils im selben Wettbewerb. Verletzungen dauern 1 bis 17 Spiele. Ausfälle werden positionsgerecht von der Bank ersetzt.
- Süper-Lig-Teams treten im Europapokal 5 Stärkepunkte schwächer an (Ligaunterschied laut UEFA-Koeffizient).

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
