'''
Author: Benjamin Fouch
Date:   May 20 2022
'''
import numpy as np
from Board import Board
from MiniMax import Minimax

def main():
    b = Board()
    m = Minimax(4)

    value = b.get_value()
    print(value)
    next_move = m.calc_move(b)

# for debugging in console w/o the visuals
def print_b(b):
    print(np.array(list(map(lambda row : list(map( lambda pos : " " if pos == 0 else np.str_(pos), row)), b))))

if __name__=="__main__":
    main()
