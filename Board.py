'''
Author: Benjamin Fouch
Date:   May 20 2022
Only "code" used: https://en.wikipedia.org/wiki/Minimax#Pseudocode
'''
import numpy as np

'''
The boards that show each state
'''
class Board:
    def __init__(self):
        self.board = np.zeros((6,7), dtype=np.int8)


    # should make it easier to plug into minimax later
    def get_board(self):
        return self.board

    def make_move(self, col, player, row=0):
        if (row == 6 or self.board[row][col] != 0):
            self.board[row-1][col] = player
        else:
            self.make_move(col, player, row=(row+1))

    def un_make_move(self, col, row=0):
        if (row == 6 or self.board[row][col] != 0):
            self.board[row][col] = 0
        else:
            self.un_make_move(col, row=(row+1))


    def winner_found(self):
        for row in self.board:
            row_str = np.array2string(row)
            if "2 2 2 2" in row_str or "1 1 1 1" in row_str:
                return True

        for row in self.board.T: # add vertival score
            row_str = np.array2string(row)
            if "2 2 2 2" in row_str or "1 1 1 1" in row_str:
                return True

        for i in range(-5, 7): # diag
            row_str = np.array2string(row)
            if "2 2 2 2" in row_str or "1 1 1 1" in row_str:
                return True

        for i in range(-5, 7): # other diag
            row_str = np.array2string(row)
            if "2 2 2 2" in row_str or "1 1 1 1" in row_str:
                return True


    # gets the value for player 1 for the current board
    # looks gross but computation effecency > nice looking code for this
    def get_value(self):
        self.value = 0
        for row in self.board: # add to values for horizontal
            self.add_values(row)

        for row in self.board.T: # add vertival score
            self.add_values(row)

        for i in range(-5, 7): # diag
            self.add_values(np.diag(self.board, i))

        for i in range(-5, 7): # other diag
            self.add_values(np.diag(self.board.T, i))

        return self.value

    def add_values(self, row):
        row_str = np.array2string(row)
        self.value += 1000000 if "1 1 1 1" in row_str else 0
        self.value += 10000 if "1 1 1" in row_str else 0
        self.value += 500 if "1 1" in row_str else 0
        self.value += 1 if "1" in row_str else 0

        self.value -= 1000000 if "2 2 2 2" in row_str else 0
        self.value -= 1000 if "2 2 2" in row_str else 0
        self.value -= 500 if "2 2" in row_str else 0
        self.value -= 1 if "2" in row_str else 0
