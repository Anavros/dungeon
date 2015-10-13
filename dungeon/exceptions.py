# coding=utf-8
# Dungeon -> Exceptions

class GameOverException(Exception):
    """Raise when the game is over.
    
    *args:
    gamewon (default: False) -- Did the player win the game?
    """

    def __init__(self, gamewon=False):
        self.gamewon = gamewon

class YouAreDeadException(Exception):
    """Raise when an actor is damaged beyond 0HP."""
