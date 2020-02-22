import math
from prettytable import PrettyTable


def f(arg):
    return arg**3-12*arg-8


def find_chord():
    
    a = -3
    b = 4
    eps = 0.0001
    x = a

    
    
    if (3*x**2-12)*(6*x) > 0:
        x0 = a
        c = b
    else:
        x0 = b
        c = a

    print("a =", a, "b =", b, "eps =", eps, "x0 =", x0)
    
    t = PrettyTable()
    t.field_names = ["x", "xi", "k"]

    k = 0
    xi = 0
    while abs(xi - x) > eps:
        x = x0
        xi = x - (f(x)*(c - x))/(f(c)-f(x))
        x0 = xi
        t.add_row([round(x, 4), round(xi, 4), k])
        k += 1

    print(t.get_string(title="f(x)"))
    return xi


def f_ind(arg):
    return arg * math.log10(arg+1) - 1


def find_chord_ind():

    a = 0
    b = 10
    eps = 0.000001
    x = b
   
    if (x+(x+1)*math.log(x+1))/((x+1)*math.log(10)) * ( (x+2)/( (x+1)*(x+1)*math.log(10) ) )  > 0:
        x0 = a
        c = b
    else:
        x0 = b
        c = a

    print("a =", a, "b =", b, "eps =", eps, "x0 =", x0)
    
    t = PrettyTable()
    t.field_names = ["x", "xi", "k"]

    k = 0
    xi = 0
    while abs(xi - x) > eps:
        x = x0
        xi = x - (f_ind(x)*(c - x))/(f_ind(c)-f_ind(x))
        x0 = xi
        t.add_row([round(x, 6), round(xi, 6), k])
        k += 1

    print(t.get_string(title="f(x) ind"))
    return xi


def main():
    a = find_chord()
    print("Answer: ", round(a, 4))
    b = find_chord_ind()
    print("Answer: ", round(b, 6))


if __name__ == "__main__":
    main()
