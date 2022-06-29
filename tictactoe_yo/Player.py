#!/usr/bin/env python import random import math
import math
import random

class Player(object):

    def __init__(self, letter):
        """
        Initialized with the letter the player is going to represent
        """
        self.letter = letter

    def next_move(self, game):
        """
        For players to get their next move
        """
        pass


class BipolarComputerPlayer(Player):
    
    def __init__(self, letter):
        # initializes super class
        super().__init__(letter)

    def next_move(self, game):
        """
        Getting a random position on the board that's empty
        """

        # Chooses one thing in a list at random
        position = random.choice(game.moves_left())
        return position


class HumanWithoutPronouns(Player):
    """
    Player should be able to choose a position on the board based on input
    passed through the terminal, and keep iterating until a valid position is
    selected.
    ---------------------------------------------------------------------------
    Valid Position is initially False
    Value is None since user hasn't input a value yet
    """
    def __init__(self, letter):
        # Initializes super class
        super().__init__(letter)

    def next_move(self, game):
        valid_move = False
        value = None

        # So user isn't confused about who's turn it is
        while not valid_move:
            position = input(self.letter + "\'s turn.\nWhat's your move? (0-9):")
            # Check via casting value to integer, where in the case that it's
            # not, it's an invalid move...
            try:
                value = int(position)
                if value not in game.moves_left():
                    raise ValueError

                valid_move = True
            except ValueError:
                print("INVALID MOVE!\nTRY AGAIN")

        return value



