import math

def f(arg):
    return arg**3 - 2 * arg**2 + 3 * arg - 5

def df(arg):
    return 3 * arg**2 - 4 * arg + 3

def ddf(arg):
    return 6 * arg - 4

a = 1
b = 2
e = 0.000001

cntA = 0
cntB = 0
x = a
xi = x-f(x)/df(x)
cntA += 1
while abs(xi - x) > e:
    x = xi
    xi = x - f(x)/df(x)
    cntA += 1
print("Answer", xi,"Count of cycles", cntA)

x = b
xi = x - f(x)/df(x)
cntB += 1
while abs(xi - x) > e:
    x = xi
    xi = x - f(x)/df(x)
    cntB += 1

print("Answer", xi,"Count of cycles", cntB)
