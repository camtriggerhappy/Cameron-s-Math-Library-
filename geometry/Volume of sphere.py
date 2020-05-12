import math


def volumeOfSphere(pi,r):
    volume = 4/3 * (pi * (r**3))
    return volume


r = float(input("What is the radius "))
pi = float(input("What are you using as pi "))

print(volumeOfSphere(pi,r))