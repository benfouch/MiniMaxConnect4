'''
Author: Benjamin Fouch
Date:   May 20 2022
Only "code" used: https://en.wikipedia.org/wiki/Minimax#Pseudocode
'''
import numpy as np
from Board import Board
from MiniMax import Minimax

'''
the game play is not perfect, but thats okay because thats not what this is about
if you want to break it, over flow a col or win at the same time as the algo
non numberic input will break it too
'''
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

if __name__=="__main__":
    main()
