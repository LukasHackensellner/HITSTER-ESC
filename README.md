# HITSTER ESC App v8 restored

Diese Version stellt die funktionierende Spotify-Verbindung aus v5 wieder her.

Enthalten:
- Spotify OAuth PKCE Login
- Refresh Token Handling
- Kamera-Scanner
- keine Anzeige von Songtitel/Interpret
- bessere Suche mit Fallback:
  1. track:"Titel" artist:"Interpret"
  2. "Titel" "Interpret"
  3. Originale QR-Suche

Wichtig:
- CLIENT_ID in index.html eintragen
- Redirect URI im Spotify Dashboard:
  https://lukashackensellner.github.io/HITSTER-ESC/
- Nach Upload am Handy Cache löschen
