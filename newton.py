import math

def f(x):
    return x**3-2*x**2+3*x-5
def df(x):
    return 3*x**2-4*x+3
def ddf(x):
    return 6*x-4
a = 1
b = 2
e = 0.000001

cntA = 0
cntB = 0
x = a
while abs(xi-x)>e:
    cntA+=1
    x = xi
    xi = x-f(x)/df(x)
print("Answer",xi," ",cntA)

x = b
while abs(xi-x)>e:
    cntB+=1
    x = xi
    xi = x-f(x)/df(x)

print("answer",xi," ",cntB)
