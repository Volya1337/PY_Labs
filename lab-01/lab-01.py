import math
from math import log, sin, pi

a = float(input('Введите а: '))
x = float(input('Введите x: '))
G = (-2*(-5*(a**2)+3*a*x+2*(x**2))) / (5*(a**2)+9*a*x-2*(x**2))
print('A = {}, X = {}, Result: {}'.format(a,x,G))

a = float(input('Введите а: '))
x = float(input('Введите x: '))
F = sin(pi*(10*(a**2)+37*a*x+7*(x**2))) / (pi*(10*(a**2)+37*a*x+7*(x**2)))
print('A = {}, X = {}, Result: {}'.format(a,x,F))

a = float(input('Введите а: '))
x = float(input('Введите x: '))
Y = log(-5*(a**2)-16*a*x+16*(x**2)+1) / log(2)
print('A = {}, X = {}, Result: {}'.format(a,x,Y))
