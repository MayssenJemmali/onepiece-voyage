# 🏴‍☠️ The Grand Voyage — One Piece Fan Web App

A fun, polished, adventure-themed web application inspired by One Piece.
Built with FastAPI, Jinja2, vanilla HTML/CSS/JS.

## Project Structure

```
onepiece-voyage/
├── main.py              # FastAPI application + all data
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Full single-page Jinja2 template
└── static/
    ├── css/
    │   └── style.css    # Complete design system
    └── js/
        └── main.js      # Stars, parallax, interactions, easter egg
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
uvicorn main:app --reload

# 3. Open in browser
# http://localhost:8000
```

## Features

- 🌊 **Hero Section** — Animated ocean waves, floating ship, star field, moon
- 👥 **Crew Section** — Character cards with images, bounties, and funny bios
- ☠️ **Wanted Board** — Tilted bounty posters pinned to a wooden tavern wall with 3D hover
- 🗺️ **Treasure Map** — Interactive nautical chart with island hovers and animated route lines
- 📖 **Adventure Log** — Timeline journal entries styled as a captain's log
- ⚓ **CTA Section** — Epic closing section with floating decorations
- 🥚 **Easter Egg** — Try the Konami code (↑↑↓↓←→←→BA)!

## Design System

- **Fonts**: Pirata One (titles), Cinzel (headings), Crimson Text (body), IM Fell English (accents)
- **Colors**: Parchment, deep ocean blues, aged gold, pirate red, ink tones
- **Aesthetic**: Nautical map + tavern wall + captain's journal

## API Endpoints

| Route | Description |
|-------|-------------|
| `GET /` | Main page |
| `GET /api/islands` | Island data as JSON |
| `GET /api/crew` | Crew data as JSON |
