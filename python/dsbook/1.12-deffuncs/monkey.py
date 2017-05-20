#!/usr/local/bin/python
'''PSwAaDS 1.12 Self Check - Inf Monkeys => Shakespeare Problem'''

import random as rand

TARGET = 'methinks it is like a weasel'
CHECK_ITER_NUM = 10000

def generate():
    '''generate a random string'''
    outstr = ''
    for _ in range(len(TARGET)):
        val = rand.randint(0, 26)
        if val == 26:
            outstr = outstr + ' '
        else:
            outstr = outstr + chr(val+ord('a'))
    return outstr

def check(instr):
    '''check if string matches target'''
    score = 0
    for i in range(len(TARGET)):
        if instr[i] == TARGET[i]:
            score = score + 1
    return score 

def main():
    '''main area'''
    done = False
    iters = 0
    highscore = 0
    highstr = ''
    while not done:
        teststr = generate()
        testres = check(teststr)
        iters = iters + 1
        if testres == len(TARGET):
            print('Perfect match after', iters, 'iterations')
            return
        elif testres >= highscore:
            highscore = testres
            highstr = teststr
        if (iters%CHECK_ITER_NUM) == 0:
            print(str(iters//CHECK_ITER_NUM), str(highscore), highstr, str(testres), teststr)


main()
