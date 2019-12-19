import math



def f(arg):
    return arg**3 - 2 * arg**2 + 3 * arg - 5

def df(arg):
    return 3 * arg**2 - 4 * arg + 3

def ddf(arg):
    return 6 * arg - 4


def newton():
    a = 1
    b = 2
    e = 0.000001
    
    cntA = 0
    cntB = 0
    x = a
    xi = x-f(x)/df(x)
    cntA += 1
    print("a =", a, "b =", b, "eps =", eps, "x0 =", x)
    while abs(xi - x) > e:
        x = xi
        xi = x - f(x)/df(x)
        cntA += 1
    print("Answer A", round(xi, 6),"Count of cycles", cntA)

    x = b
    xi = x - f(x)/df(x)
    cntB += 1
    while abs(xi - x) > e:
        x = xi
        xi = x - f(x)/df(x)
        cntB += 1

    print("Answer B", round(xi, 6),"Count of cycles", cntB)


def f_ind(arg):
    return arg * math.log10(arg+1) - 1

def df_ind(arg):
    return (arg+(arg+1)*math.log(arg+1))/((arg+1)*math.log(10))

def ddf_ind(arg):
    return (arg+2)/((arg+1)*(arg+1)*math.log(10))

def ind_newton():
    a = 0
    b = 10
    e = 0.000001

    cntB = 0
  
    x = b
    xi = x - f_ind(x)/df_ind(x)
    cntB += 1
    
    print("a =", a, "b =", b, "eps =", eps, "x0 =", x)
    
    while abs(xi - x) > e:
        x = xi
        xi = x - f_ind(x)/df_ind(x)
        cntB += 1

    print("Answer B", round(xi, 6),"Count of cycles", cntB)


def main():
    print("x^3-2*x^2+3*x-5=0")
    newton()
    
    print("x*lg(x+1)=1")
    ind_newton()

if __name__ == "__main__":
    main()
