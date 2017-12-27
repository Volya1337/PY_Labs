# Импорт математической библиотеки #

import math
from math import log, sin, pi

# Ввод значений а и х #

a = float(input("Введите а: "))
x = float(input("Введите x: "))

# Выбор формулы #

print(" 1 - Вычислить функцию G\n "
      " 2 - Вычислить функцию F\n "
      " 3 - Вычислить функцию Y\n ")
num1 = float(input('Значение'))
if num1 == 1:
    if (x != 0) and (a != 0):
        G = (-2*(-5*(a**2)+3*a*x+2*(x**2))) / (5*(a**2)+9*a*x-2*(x**2))
        print('A = {}, X = {}, Result: {}'.format(a,x,G))
    else:
        print(" Введите корректное значение ")
elif num1 == 2:
    F = sin(pi*(10*(a**2)+37*a*x+7*(x**2))) / (pi*(10*(a**2)+37*a*x+7*(x**2)))
    print('A = {}, X = {}, Result: {}'.format(a,x,F))
elif num1 == 3:
    if (a < 0):
        Y = log(-5*(a**2)-16*a*x+16*(x**2)+1) / log(2)
        print('A = {}, X = {}, Result: {}'.format(a,x,Y))
    else:
         print(" Введите отрицательное число ")
else:
        print("Нет такого значения")
       
