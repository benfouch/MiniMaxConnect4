'''
Author: Benjamin Fouch
Date:   May 20 2022
'''
import numpy as np
from Board import Board
from MiniMax import Minimax

def main():
    b = Board()
    m = Minimax()

    while not b.winner_found():
        print("Pick a row between 0 and 6: ")
        i = input()
        if int(i) <= 7 and not i.startswith("-"):
            b.make_move(int(i), 2)
            print(b.get_board())

            next_best_m = m.find_best(b)
            b.make_move(next_best_m[0], 1)
            print((next_best_m))
            print(b.get_board())
        else :
            print("Enter a valid move")

    print("GAME OVER")



# for debugging in console w/o the visuals
def print_b(b):
    print(np.array(list(map(lambda row : list(map( lambda pos : " " if pos == 0 else np.str_(pos), row)), b))))

if __name__=="__main__":
    main()
