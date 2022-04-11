import decimal


def newtonsAlgorithm(initGuess: decimal.Decimal, function):
    x0 =decimal.Decimal(initGuess)
    step = 1
    x1 = decimal.Decimal(.00000001)
    while (abs(step) > decimal.Decimal(.00000001)):
        derivative = (function(x0 + x1) - function(x0))/x1
  
        step = function(x0)/derivative
        x0 = x0 - step

    return x0


def function(xVal:decimal.Decimal):
    return xVal ** 2 -1

newtonsAlgorithm(4, function)

