# HITSTER ESC App v3

Fix für `invalid track uri`.

Diese Version:
- behandelt nur `spotify:track:<22 Zeichen>` als direkten Track
- löst `?q=Artist Titel` zuerst über die Spotify Search API auf
- konvertiert alte `spotify:search:`-Werte automatisch in Suchanfragen
- nutzt den aktuellen QR-Code vor alten localStorage-Werten
- enthält einen „Cache löschen“-Button

## Deployment

1. In `index.html` deine Spotify Client ID eintragen.
2. Datei in dein GitHub-Pages-Repo `HITSTER-ESC` hochladen/ersetzen.
3. Im Spotify Developer Dashboard muss als Redirect URI stehen:
   `https://lukashackensellner.github.io/HITSTER-ESC/`
4. Nach dem Upload auf dem Handy einmal die Seite öffnen und „Cache löschen“ klicken.
