import math

def IsRight(a,b,c):
    
    if a**2 + b**2 > c**2 or a**2 + b**2 < c**2:
        print("Not Possible")
    elif a**2 + b**2 == c**2:
        print("Possible")

A = float(input("What is A "))
B = float(input("What is B "))
C = float(input("What is C "))

IsRight(A,B,C)