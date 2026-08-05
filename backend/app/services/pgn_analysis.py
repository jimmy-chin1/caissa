#!/usr/bin/env python3

"""Utilities for parsing and analysing PGN games"""

import logging

import chess.pgn

logger = logging.getLogger(__name__)


def parse_pgn(pgn_path: str) -> list[chess.pgn.Game]:
    """Parse a PGN file and return a list of games
    https://python-chess.readthedocs.io/en/latest/pgn.html"""

    # PGN files are usually ASCII or UTF-8 encoded, sometimes with BOM (which this
    # parser automatically ignores)
    try:
        with open(pgn_path, mode="r", encoding="utf-8") as pgn:
            games = []
            while True:
                game = chess.pgn.read_game(handle=pgn)
                if not game:
                    break

                if game.errors:
                    logger.warning(
                        "PGN parsing errors for %s: %s", pgn_path, game.errors
                    )

                games.append(game)
    except FileNotFoundError as err:
        raise ValueError("PGN file was not found") from err

    return games
