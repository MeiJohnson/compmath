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
 
  t = PrettyTable()
  t.field_names = ["xi", "x", "k"]
  
  k = 0
  xi = 0
  while abs(xi - x) > eps:
      x = x0
      xi = x - (f(x)*(c - x))/(f(c)-f(x))
      x0 = xi
      t.add_row([round(xi,7), x,k])
      k += 1
      
  print(t.get_string(title="f(x)"))
  return xi


def main():
  a = find_chord()

if __name__ == "__main__":
  main()