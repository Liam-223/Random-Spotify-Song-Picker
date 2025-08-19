# Random Spotify Song Picker

A single‑file web app that logs into your Spotify account and picks a truly random song from your Liked Songs or any of your playlists.

## What’s inside
- `index.html` — the entire app (no backend required). Your Client ID is already set in the file.
- `start_server.py` — tiny helper that serves the app on http://127.0.0.1:8000 and opens your browser.

## One‑time setup (Spotify dashboard)
1. Go to https://developer.spotify.com/dashboard → your app.
2. In **Settings → Redirect URIs**, add **`http://127.0.0.1:8000/index.html`** (or whatever URL you plan to use).
3. Save.

> You don’t need a client secret for this flow.

## Run it
Option A — with the included script:
```
python3 start_server.py
```
This starts a local server and opens your browser to the correct URL.

Option B — any static server:
```
python3 -m http.server 8000
# then open http://127.0.0.1:8000/index.html
```

## Use it
1. Click **Log in with Spotify** and approve.
2. Choose **Liked Songs** or switch to **Playlist** and pick one.
3. Hit **Pick random**. Use **Roll again** as much as you like.

## Notes
- Tokens are stored in your browser’s localStorage and expire periodically. If it stops working, log in again.
- If you change the port or path, add that exact URL to the Redirect URIs list in your Spotify app settings.
- Not affiliated with Spotify.
