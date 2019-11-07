import math

def f(l, x, y):
  return eval(l)

def getData():
  data = open("/home/vasya/Документы/Github/wm/difurProj/a.in")
  
  data_list = []
  for line in data:
    data_list.append(line)
  
  l = data_list[0]
  print("Введите функцию ", l, end = "")

  a = float(data_list[1])
  print("Введите a ", a)
  
  b = float(data_list[2])
  print("Введите b ", b)

  y0 = float(data_list[3])
  print("Введите y0 ", y0)
  
  n = float(data_list[4])
  print("Введите n ", n)
  
  h = (b - a) / n
  data.close()
  
  res = [l, a, b, y0, n, h]

  return res

def eiler():
  src = getData()
  print("x = ",src[1],"y = ", src[3], "h = ", src[5])
  x = src[1]
  y = src[3]
  
  eps = src[2] - src[5]
  
  while x <= eps:
    print("x = ",round(x, 3), "y = ",round(y, 3))
    y += src[5] * f(src[0], x, y)
    x += src[5]
  
  submenu()  
  
def Fi(x, y, h, l):
  k1 = h * f(l, x, y)
  k2 = h * f(l,x + h / 2, y + k1 / 2)
  k3 = h * f(l, x + h / 2, y + k2 / 2)
  k4 = h * f(l, x + h, y + k3)
  return (k1 + 2 * k2 + 2 * k3 + k4) / 6

def runge():
  src = getData()
  x = src[1]
  y = src[3]
  eps = src[2] - src[5]

  while x <= eps:
    print("x = ", round(x, 3), "y = ", round(y, 3))
    y += Fi(x, y, src[5], src[0])
    x += src[5]
    
  
  submenu()
  

def high_order():
  a = float(input("Введите a "))
  b = float(input("Введите b "))
  h = float(input("Введите h ")) 
  x = a
  y = float(input("Введите y(1) "))
  z = float(input("Введите y'(1) "))
  
  while x < b:
    y1 = y
    print("x = ", round(x, 5), "z = ", round(z, 5), "y = ", round(y, 5))
    y += h * z
    z -= h * (z / x + y1)
    x += h
    
  submenu()
  
def systemUr():
  h = float(input("Введите h ")) 
  t = float(input("Введите a "))
  b = float(input("Введите b "))
  x = float(input("Введите х(1) "))
  y = float(input("Введите y(1) "))
  z = float(input("Введите z(1) "))

  while t < b:
     print("t = ", round(t, 5), "x = ", round(x, 5), "z = ", round(z, 5), "y = ", round(y, 5))
     x0 = x
     y0 = y
     z0 = z
     x += h * (-2 * x0 + 5 * z0)
     y += h * (math.sin(t - 1) * x0 - y0 + 3 * z0)
     z += h * (-x0 + 2 * z0)
     t += h
  
  submenu()


def menu(): 

  print("Главное меню")
  print("1.Метод Эйлера")
  print("2.Метод Рунге-Кутта")
  print("3.Решение уравнения втрого порядка")
  print("4.Решение систем диф. уравнений")
  print("5.Выход")
  
  num = int(input("Введите номер "))
  
  if num == 1:
    eiler()
  if num == 2:
    runge()
  if num == 3:
    high_order()
  if num == 4:
    systemUr()
  if num == 5:
    exit()

def submenu(): 
  print("Подменю")
  print("1.В главное меню")
  print("2.Выход")
  num = int(input("Введите номер "))
  if num == 1:
      menu()
  if num == 2:
      exit()

def main():
  menu()
  

if __name__ == "__main__":
  main()