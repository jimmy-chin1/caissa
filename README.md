# Caissa

**Status: Early development. The initial PGN analysis prototype is currently being implemented.
**
Caissa is a personalised chess coach that analyses PGN games with Stockfish and transforms a player's mistakes into interactive training puzzles.

## Project Goal

The goal of Caissa is to help chess players improve using positions from their own games rather than generic puzzle sets.

Caissa will:

* Analyse uploaded PGN games
* Identify mistakes and blunders
* Show the strongest alternative move
* Generate puzzles from meaningful mistakes
* Track recurring weaknesses
* Build personalised training sessions

## Initial Milestone

The first version will accept a PGN file and player name, analyse the game with Stockfish, and return the player's three largest evaluation losses.

Each result will include:

* Move number
* Move played
* Best move
* Evaluation loss
* Mistake classification
* Principal variation

## Planned Technology

### Backend

* Python
* FastAPI
* python-chess
* Stockfish

### Frontend

* React
* TypeScript
* Vite

### Infrastructure

* PostgreSQL
* Redis
* Docker
* GitHub Actions

## Planned Project Structure

```text
caissa/
├── backend/
│   └── prototype/
│       ├── analyse_game.py
│       ├── sample_game.pgn
│       └── requirements.txt
├── frontend/
├── README.md
└── .github/
    └── workflows/
```

## Status

Caissa is currently in early development. The initial focus is building a reliable PGN and Stockfish analysis pipeline before adding the full web interface, personalised training algorithms, and AI-generated explanations.

## Roadmap

* [ ] Parse uploaded PGN games
* [ ] Detect the player's colour
* [ ] Analyse positions using Stockfish
* [ ] Identify the three largest evaluation losses
* [ ] Export analysis results as JSON
* [ ] Create a FastAPI analysis endpoint
* [ ] Build a React interface
* [ ] Generate interactive puzzles
* [ ] Deploy a public demonstration
