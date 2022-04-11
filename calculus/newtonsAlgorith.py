from threading import Thread
import time


def newtonsAlgorithm(initGuess: float, function):
    x0 = initGuess
    step = 1
    while (abs(step) > .001):
        derivative = (function(x0 + .00001) - function(x0))/.00001
        step = function(x0)/derivative
        x0 = x0 - step


def function(xVal):
    return xVal ** 2 -1

newtonsAlgorithm(4, function)

