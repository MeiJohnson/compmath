import math

a_values_exp = [0.9999998, 1.000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
a_values_sin = [1.000000002, -0.166666589, 0.08333075, -0.000198107, 0.000002608]

def f(l, a, x):
  return a*x

def elementary():
  k = 0
  x = 0.5 
  p = 1
  sum_i = a_values_exp[k]
  print("res = ", round(sum_i, 7), "k = ", k, "x = ",p )
  k += 1
  eps = 0.0000002
  for el in range(1,8):
    p *= x
    sum_i += a_values_exp[k]*p
    print("res = ", round(sum_i, 7), "k = ", k, "x = ",p )
    k += 1
  return sum_i 

def main():
  print("Final result = ",round(elementary(),7), "\nexp ", math.exp(0.5))
  

if __name__ == "__main__":
  main()