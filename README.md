# HITSTER ESC App v2

Diese Version kann zwei QR-Code-Formate:

- `?track=spotify:track:TRACK_ID` für echte feste Track-IDs
- `?q=Artist Titel` für automatische Spotify-API-Suche und sofortiges Abspielen des ersten Treffers

Für dein vollständiges ESC-Deck sind die QR-Codes auf `?q=` gesetzt, damit keine falschen statischen Track-IDs verwendet werden.

## Einrichtung

1. In `index.html` `DEINE_SPOTIFY_CLIENT_ID_HIER` ersetzen.
2. In Spotify Developer Dashboard als Redirect URI eintragen:
   `https://lukashackensellner.github.io/HITSTER-ESC/`
3. Datei in dein GitHub-Pages-Repo hochladen.
4. Spotify Premium und ein aktives Spotify-Gerät sind erforderlich.
