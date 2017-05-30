#!/usr/local/bin/python
'''fraction class for learning oop'''

class Fraction(object):
    '''pure fraction implementation'''
    def __init__(self, top, bot):
        self.num = top
        self.den = bot

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + other.num * self.den
        newden = self.den * other.den
        comden = gcd(self.den, other.den)
        return Fraction(newnum//comden, newden//comden)

def gcd(den1, den2):
    '''find greatest common denominator'''
    while den1 % den2 != 0:
        prevden1 = den1
        prevden2 = den2
        den1 = prevden2
        den2 = prevden1%prevden2
    return den2

def main():
    '''main area'''
    frac1 = Fraction(1, 2)
    frac2 = Fraction(1, 4)
    frac3 = frac1 + frac2
    print frac1
    print frac2
    print frac3

main()
