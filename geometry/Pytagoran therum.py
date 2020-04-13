import math



def Pythagorean(a,b,c):
    if a == 0:
        a = c**2 - b**2
        a = math.sqrt(a)
        print(a)

    if b == 0:
        b = c**2 - a**2
        b = math.sqrt(b)
        print(b)

    if c == 0:
        c = a**2 + b**2
        c = math.sqrt(c)
        print(c)

a = float(input("what is a "))
b = float(input("what is b "))
c = float(input("what is c "))
Pythagorean(a,b,c)