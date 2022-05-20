'''
Author: Benjamin Fouch
Date:   May 20 2022
'''
import numpy as np

# TOPO: Make static? could just pass in depth each time instead
class Minimax:
    def __init__(self, depth):
        self.d = depth

    def calc_move(self, board):# -> np.array
        print("test")
