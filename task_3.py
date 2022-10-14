def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    def __add__(self, other_fraction):
        newnum = self.num * other_fraction.den + self.den * other_fraction.num
        newden = self.den * other_fraction.den
        
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __sub__(self, other_fraction):
        newnum = self.num * other_fraction.den - self.den * other_fraction.num
        newden = self.den * other_fraction.den
        
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden / common)
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum


    def __str__(self):
        return str(self.num) + "/" + str(self.den)


f1 = Fraction(2, 3)
f2 = Fraction(3, 9)

print(f1 + f2)
