'''
Author: Benjamin Fouch
Date:   May 20 2022
Only "code" used: https://en.wikipedia.org/wiki/Minimax#Pseudocode
'''
import numpy as np
import copy

'''
Mini max algo with Alpha beta pruning
'''
class Minimax:
    def find_best(self, board):
        print("Col: Score:")
        best_tup = (-1, float('-inf'))
        for i in range(7):
            board.make_move(i, 1)
            val = self.calc_vals(board, 4, True, float('-inf'), float('inf'))
            board.un_make_move(i)

            print(i, val)

            if best_tup[1] < val:
                best_tup = (i, val)

        return best_tup


    def calc_vals(self, board, depth, maxingPlayer, a, b):
        if depth == 0 or board.winner_found():
            return board.get_value()
        if maxingPlayer:
            value = float('-inf')
            for i in range(7):
                if not board.winner_found():
                    board.make_move(i, 1)
                    next_v = self.calc_vals(copy.deepcopy(board), depth-1, False, a, b)
                    value = next_v if next_v > value else value
                    board.un_make_move(i)
                    if value >= b:
                        break
                    a = a if a > value else value

            return value
        else:
            value = float('inf')
            for i in range(7):
                if not board.winner_found():
                    board.make_move(i, 2)
                    next_v = self.calc_vals(copy.deepcopy(board), depth-1, True, a, b)
                    value = next_v if next_v < value else value
                    board.un_make_move(i)
                    if value <= a:
                        break
                    b = b if b < value else value

            return value
