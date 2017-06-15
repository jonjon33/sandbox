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
        comden = gcd(newnum, newden)
        return Fraction(newnum//comden, newden//comden)

    def __sub__(self, other):
        newnum = self.num * other.den - other.num * self.den
        newden = self.den * other.den
        comden = gcd(newnum, newden)
        return Fraction(newnum//comden, newden//comden)

    def __mul__(self, other):
        newnum = self.num *  other.num
        newden = self.den * other.den
        comden = gcd(newnum, newden)
        return Fraction(newnum//comden, newden//comden)

    def __div__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        comden = gcd(newnum, newden)
        return Fraction(newnum//comden, newden//comden)

    def __eq__(self, other):
        val1 = self.num * other.den
        val2 = self.den * other.num
        return val1 == val2

    def __lt__(self, other):
        val1 = self.num * other.den
        val2 = self.den * other.num
        return val1 < val2

    def __gt__(self, other):
        val1 = self.num * other.den
        val2 = self.den * other.num
        return val1 > val2

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
    frac4 = frac1 - frac2
    frac5 = frac2 - frac3
    frac6 = frac1 * frac2
    frac7 = frac2 / frac1

    print frac1
    print frac2
    print frac3
    print frac4
    print frac5
    print frac6
    print frac7
    print frac1 == frac7
    print frac1 > frac2
    print frac2 < frac3
    print frac1 == frac2
    print frac2 > frac3
    print frac1 < frac2

main()
