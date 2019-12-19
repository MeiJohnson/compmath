import math
from prettytable import PrettyTable

a_values_exp = [0.9999998, 1.000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
a_values_sin = [1.000000002, -0.166666589, 0.08333075, -0.000198107, 0.000002608]

def find_exp():
  #Находим exp(0.5) методом Чебышева
  k = 0
  x = 0.5 
  p = 1
  summa = 0
  sum_i_exp = a_values_exp[k]*p
  
  t = PrettyTable()
  t.field_names = ["sums", "k"]
  t.add_row([round(sum_i_exp,7), k])

  eps = 0.000002 # точность -7 не подходит
  k += 1

  while k < len(a_values_exp):
    while abs(summa - sum_i_exp) > eps:
        p *= x
        summa = sum_i_exp
        sum_i_exp += a_values_exp[k]*p
        t.add_row([round(sum_i_exp,7), k])
        k += 1
  print(t.get_string(title="Exp(0.5)"))
  return sum_i_exp

def find_sin():  
  #Находим sin(pi/6) методом Чебышева
  k = 0
  x = math.pi/6
  eps = 0.00000006
  summa = 0
  sum_i_sin = a_values_sin[k]*x**(2*k+1)
  
  t = PrettyTable()
  t.field_names = ["sums", "k"]
  t.add_row([round(sum_i_sin,9), k*2+1])

  k += 1

  while k < len(a_values_sin):
    while abs(summa - sum_i_sin) > eps:
        summa = sum_i_sin
        sum_i_sin += a_values_sin[k]*x**(2*k+1)
        t.add_row([round(sum_i_sin,9), k*2+1])
        k += 1
  print(t.get_string(title="Sin(pi/6)"))
  return sum_i_sin

def row_ln():
    #Находим ln(0.5) разложением в ряд
  n = 1
  x = 0.5
  summa = 0
  eps = 0.000001
  summa_i = ((-1)**(n+1)*x**n)/n
  
  t = PrettyTable()
  t.field_names = ["sums", "n"]
  t.add_row([round(summa_i,7), n])
  while abs(summa - summa_i) > eps:
    summa = summa_i
    n+=1
    y = ((-1)**(n+1)*x**n)/n
    summa_i+=y
    t.add_row([round(summa_i,7), n])
  print(t.get_string(title="Ln(1.5)"))
  return summa_i

def row_arctg():
    #Находим arctg(pi/6) разложением в ряд
  n = 0
  x = math.pi/6
  summa = 0
  eps = 0.000001
  summa_i = ((-1)**n*x**(2*n+1))/(2*n+1)

  t = PrettyTable()
  t.field_names = ["sums", "n"]
  t.add_row([round(summa_i,7), n])
 
  while abs(summa - summa_i) > eps:
    summa = summa_i
    n+=1
    y = ((-1)**n*x**(2*n+1))/(2*n+1)
    summa_i+=y
    t.add_row([round(summa_i,7), n])
  print(t.get_string(title = "Arctg(pi/6)"))
  return summa_i

def main():
  print("Exp(0.5)")
  a = find_exp()
  print("Sin(pi/6)")
  b = find_sin()
  print("Ln(0.5)")
  c = row_ln()
  print("Arctg(pi/6)")
  d = row_arctg()

if __name__ == "__main__":
  main()