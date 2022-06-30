#!/usr/bin/env python
#from Player import *                       LEFT OFF AT 57:52 of the YT video

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




class TicTacToe(object):

    def __init__(self):
        """
        board: 3x3 Board, as list of length nine, assigning and INDEX to each of the positions

        the_winner: Monitors whether or not there's a winner, and if so, who 
        """
        self.board = [' ' for _ in range(9)]
        the_winner = None

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

            if self.winner(position, letter):
                self.the_winner = letter
            return True

        return False

    def winner(self, position, letter):
        """
        Checks if there's three in row of each letter; Diagonal, Horizontal, or
        Vertical
        """

        # Row: whatever position divided by three, rounded DOWN
        row_index = position // 3
        # Given the row index, get the row
        # List of items in the row that's selected
        row = self.board[row_index*3: (row_index + 1) * 3]

        if all([position == letter for position in row]):
            return True

        # Column:
        column_index = position % 3
        column = [self.board[column_index+i*3] for i in range(3)]
        if all([position == letter for position in column]):
            return True

        # Diagonals
        """
        From left-up to right-down, Up-right to left-down: EVEN NUMBERS 
        """
        if position % 2 ==0:
            neg_slope = [self.board[i] for i in [0, 4, 8]]
            if all([position == letter for position in neg_slope]):
                return Truel

            pos_slope = [self.board[i] for i in [2, 4, 6]]
            if all([position == letter for position in pos_slope]):
                return True

        # No winner
        return False

def play(game, x_player, o_player, print_game):
    """
    Main Play function of the game.
    Returns the letter of winner or None if it's a tie
    ----------------------------------------------------------------------
    INPUTS:
        game: 
        x_player
        o_player
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
            position = o_player.next_move(game)

        else:
            position = x_player.next_move(game)

        
        # Making moves
        if game.make_a_move(position, letter):
            if print_game:
                print(letter + f"Makes a move to position {position}")
                game.display_board()
                print('')

            if game.winner:
                if print_game:
                    print(f"{letter} wins!\n")

        # After the move, alternate letters (swapping players, basically)
        letter = '0' if letter == 'X' else 'X'
#        if letter == 'X':
#            letter = '0'
#
#        else:
#            letter = 'X'

        if print_game:
            print("TIE!\n (ಥ ͜ʖಥ)")


if __name__ == "__main__":
    x_player = HumanWithoutPronouns('X')
    o_player = BipolarComputerPlayer('O')
    tictactoe = TicTacToe()
    play(tictactoe, x_player, o_player, True)


