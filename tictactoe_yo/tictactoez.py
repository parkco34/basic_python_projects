#!/usr/bin/env python

"""
Tic Tac Toe Commmand Line Game:
Players can be:
    1) Human-to-Computer
    2) Computer-to-Computer
    3) Human-to-Human

Game is separated into twos separate Classes:
    1) Player
        X player
        O player

        Base Player Class

    2) Game

INHERITANCE used to create a random computer player and a human computer player
that builds on top of the base player
"""




class TicTacToez(object):

    def __init__(self, board):
        """
        board: 3x3 Board, as list of length nine, assigning and INDEX to each of the positions

        winner: Monitors whether or not there's a winner, and if so, who 
        """
        self.board = board

    def display_board(self):
        """
        Groups of three positions, where
        First row: 0, 1, 2
        Second row: 3, 4, 5
        Third row: 6, 7, 8
        --------------------------------
        Replace this with a PROPER board
        """

        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def display_numbers_on_board():
        """
        Doesn't have any relevance in terms of a specific kind of board
        It just do what it does, yo... ( ͡° ل͜ ͡°)
        Prints out which numbers coresspond to the positions fo the board,
        giving each position an identity based on the board numbers
        ------------------------------------------------------------
        Getting each of the indices in the rows for each of the rows (e.g.
        0,1,2; 3, 4, 5; 6, 7, 8 ... )
        """
        
        numbers = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numbers:
            print('|' + '|'.join(row) + '|')

    def moves_left(self):
        """
        Given the recent move, what moves are available on the board?
        -------------------------------------------------------------
        If given position is empty (' '), then it's an available move that can
        be made, and we add it the list of available moves.
        -------------------------------------------------------------
        INPUTS:
            None

        OUTPUTS:
            Returns a (list) of Indices
            
        """
        
        return [idx for idx, pos in enumerate(self.board) if pos == ' ']
#        moves = []
#        for (idx, pos) in enumerate(self.board):
#            if pos == ' ':
#                moves.append(idx)
#            return moves

    def empty_positions(self):
        """
        Checks if there are any empty positions on the board
        ----------------------------------------------------
        INPUTS:
            None

        OUTPUTS:
            Returns a (bool)
        """

        return ' ' in self.board

    def number_of_empty_positions(self):
        """
        Get the number of empty positions
        ---------------------------------
        INPUTS:
            None

        OUTPUTS:
            Returns an (int) via len()
        """

        return len(self.moves_left())
#        return self.board.count(' ')

    def make_a_move(self, position, letter):
        """
        Ensures the position that the player wants to their next selection to
        be is good and proper, and what letter the player is
        --------------------------------------------------------------------
        INPUTS:
            position:
            letter:

        OUTPUTS:
            Returns a (bool) whether the move is valid or not
            Returns True if move is valid, and False if it's not...
        """

        if self.board[position] == ' ':
            self.board[position] = letter
            return True

        return False

def play(game, X_player, O_player, print_game):
    """
    INPUTS:
        game: 
        X_player
        O_player
        print_game: (bool) If True, Human-to-Computer, where all the steps are
        printed.  Otherwise, the steps of the game are omitted since it will be
        Computer-to-Computer.

    OUTPUTS:

    """
    
    if print_game:
        game.display_numbers_on_board()

    # Starting letter:
    letter = 'X'
    """
    Continue to iterate until there are no empty positions on the board
    """
    while game.empty_positions():
        # Get the moves from the correct player
        if letter == '0':
            position = O_player.next_move(game)

        else:
            position = X_player.next_move(game)

        
        # Making moves
        if game.make_a_move(position, letter):
            if print_game:
                print(letter + f"Makes a move to position {position}")
                game.print_board()
                print('')

        # After the move, alternate letters
        letter = '0' if letter == 'X' else 'X'
#        if letter == 'X':
#            letter = '0'
#
#        else:
#            letter = 'X'

        """
        What if a player won??
        Probably should be right after one of the players makes a move...
        """

