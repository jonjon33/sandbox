#!/usr/local/bin/python
'''PSwAaDS 1.12 Self Check - Inf Monkeys w/ Hill Climb'''

import random as rand

TARGET = 'methinks it is like a weasel'

def generate(instr, matchset):
    '''generate based on matchset'''
    outstr = ''
    for i, _ in enumerate(TARGET):
        if i in matchset:
            outstr += instr[i]
        else:
            val = rand.randint(0, 26)
            if val == 26:
                outstr += ' '
            else:
                outstr += chr(val+ord('a'))
    return outstr

def check(instr):
    '''check and update matchset'''
    matchlist = []
    for i, _ in enumerate(TARGET):
        if instr[i] == TARGET[i]:
            matchlist.append(i)
    return matchlist

def main():
    '''main area'''
    done = False
    ctr = 0
    workingstr = ''
    matchlist = []
    while not done:
        workingstr = generate(workingstr, matchlist)
        matchlist = check(workingstr)
        ctr = ctr + 1
        print str(ctr), str(len(matchlist)), workingstr
        if len(matchlist) == len(TARGET):
            print 'Perfect match after', ctr, 'iterations'
            return

main()
