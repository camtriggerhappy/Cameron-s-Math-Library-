import math

def IsRight(a,b,c):
    
    if a**2 + b**2 > c**2 or a**2 + b**2 < c**2:
        print("Not Possible")
        return False
    elif a**2 + b**2 == c**2:
        print("Possible")
        return True

A = float(input("What is A "))
B = float(input("What is B "))
C = float(input("What is C "))

IsRight(A,B,C)