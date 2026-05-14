# ESC HITSTER Spotify Player

Diese Mini-Web-App startet Spotify-Tracks über die Spotify Web API.

## Voraussetzungen

- Spotify Premium
- Aktives Spotify-Gerät, z. B. Spotify-App am Handy geöffnet
- Spotify Developer App
- Gehostete HTTPS-Seite, z. B. Netlify, Vercel, GitHub Pages

## Einrichtung

1. Öffne https://developer.spotify.com/dashboard
2. Erstelle eine App
3. Trage als Redirect URI die URL deiner gehosteten Seite ein, z. B.
   `https://dein-name.github.io/esc-hitster/`
4. Kopiere die Client ID
5. Öffne `index.html`
6. Ersetze:
   `DEINE_SPOTIFY_CLIENT_ID_HIER`
   durch deine Client ID
7. Lade die Datei auf deine Website hoch

## QR-Code Format

Jeder QR-Code muss auf deine App zeigen:

`https://deine-domain.example/?track=spotify:track:TRACK_ID`

Beispiel:

`https://deine-domain.example/?track=spotify:track:3Dy4REq8O09IlgiwuHQ3sk`

## Wichtig

Beim ersten Scan muss Spotify einmal autorisiert werden.
Danach kann die App Tracks direkt auf dem aktiven Spotify-Gerät starten.
