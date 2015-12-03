# coding=utf-8
# Dungeon -> Exceptions

class YouAreDeadException(Exception):
    """Raise when an actor is damaged beyond 0HP."""
    
    def __init__(self, game_won=False):
        self.game_won = game_won
