'''sudokusolver'''
from __future__ import print_function # want that end=''
import numpy as np # using ndarray instead of a traditional array/list

class Sudoku(object):
    '''sudoku game state and solver class'''
    def __init__(self):
        '''initialize the board and vars'''
        opt = input('choose game method:\n'+ \
                    ' 1) built-in puzzle\n'+ \
                    ' 2) rng puzzle\n'+ \
                    ' 3) user puzzle\n')
        # switch game modes
        if opt == 1:
            puzzle = input('select puzzle (1-2):')
            # switch puzzles
            if puzzle == 1:
                self.state = np.array([[0,3,0,2,9,7,0,0,4], \
                                       [5,0,0,0,3,0,6,2,7], \
                                       [0,0,0,0,6,0,0,9,0], \
                                       [0,0,8,0,5,0,0,7,1], \
                                       [7,9,0,0,0,0,0,4,5], \
                                       [4,5,0,0,2,0,8,0,0], \
                                       [0,7,0,0,8,0,0,0,0], \
                                       [9,1,5,0,7,0,0,0,8], \
                                       [2,0,0,5,4,9,0,1,0]])
            elif puzzle == 2:
                self.state = np.array([[0,3,7,0,2,0,0,0,0], \
                                       [0,0,0,6,9,0,0,0,3], \
                                       [0,0,0,0,0,0,0,9,8], \
                                       [0,2,8,0,0,0,0,0,0], \
                                       [4,0,0,1,0,3,0,0,7], \
                                       [0,0,0,0,0,0,4,8,0], \
                                       [7,5,0,0,0,0,0,0,0], \
                                       [1,0,0,0,4,9,0,0,0], \
                                       [0,0,0,0,6,0,7,4,0]])
            else:
                print('no puzzle at given index!')
                exit()
        else:
            print("this option is TODO!")
            exit()

        self.potentials = {}
        self.stepcount = 0
        self.maxdepth = 0

    def solve(self):
        '''solver loop that checks, steps, and prints'''
        self.checkboard()
        while not self.solvestep():
            self.show()
            self.checkboard()
            if len(self.potentials) == 0:
                print('solved in '+str(self.stepcount)+' steps!')
                print('max assumption depth was '+str(self.maxdepth)+' levels')
                return
        print(self.potentials) # get info if solvestep() fails

    def checkboard(self):
        '''iterate through board writing potentials dict'''
        for i,row in enumerate(self.state):
            for j,item in enumerate(row):
                if self.state[i,j] == 0:
                    self.potentials[(i,j)] = self.checkcell((i,j))

    def solvestep(self):
        '''single step of solve procedure, non-zero return of errors'''
        hit = False
        self.stepcount = self.stepcount + 1
        for coord in self.potentials.keys():
            if len(self.potentials[coord]) == 1:
                hit = True
                (x,y) = coord
                self.state[x,y] = self.potentials[coord].pop()
                del self.potentials[coord]
        if hit == False:
            print("Warning: no 1-len cells")
            return 1
        return 0

    def checkcell(self,coord):
        '''return list of potential legal cell contents'''
        (x,y) = coord
        potlist = range(1,10)

        # check the row
        for val in self.state[x]:
            if val in potlist:
                potlist.remove(val)

        # check the column
        for row in self.state:
            val = row[y]
            if val in potlist:
                potlist.remove(val)

        # check the box
        for i in range(3):
            currow = x + i - (x % 3)
            for j in range(3):
                curcol = y + j - (y % 3)
                val = self.state[currow,curcol]
                if val in potlist:
                    potlist.remove(val)

        return potlist


    def show(self):
        '''print the board in a human-readable manner'''
        print()
        for i,row in enumerate(self.state):
            if i % 3 == 0 and i != 0:
                print('---------------------')
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print('| ',end='')
                print(convchar(row[j])+' ',end='')
            print()
        print()

def convchar(num):
    '''helper to make state values easier to read on board'''
    if num == 0:
        return '.'
    else:
        return str(num)


def main():
    '''main area'''
    game = Sudoku()
    game.show()
    game.solve()

main()
