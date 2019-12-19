import math
from prettytable import PrettyTable

def f_ind(arg):
    return arg * math.log10(arg+1) - 1


def bisec():
    a = 0
    b = 10
    eps = 0.000001
    print("a =", a, "b =", b, "eps =", eps)
    
    t = PrettyTable()
    t.field_names = ["x", "y"]
    
    while (b-a) > eps:
        xd = (b - a)/2
        xi = a+xd
        if f_ind(a)*f_ind(xi) < 0:
            b = xi
        else:
            a = xi
        t.add_row([round(xi, 6), round(f_ind(xi), 6)])
    t.align = "l"
    print(t.get_string(title="f(x) ind"))
    return xi 
    
    
    
def main():
    a = bisec()
    print("Answer: ", round(a, 6))


if __name__ == "__main__":
    main()