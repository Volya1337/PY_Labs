from math import log, sin, pi, isclose
# Выбор формулы #

res = []


print(" 1 - Вычислить функцию G\n "
      " 2 - Вычислить функцию F\n "
      " 3 - Вычислить функцию Y\n "
      " 0 - Выход из программы \n ")
num1 = float(input('Значение\n'))
if num1 == 0:
    print("До свидания!")
else:
    a = float(input("Введите а: "))

    x_min = float(input("Введите минимальное значение x: "))

    x_max = float(input("Введите макимальное значение х: "))

    step_c = int(input("Введите число шагов: "))
    step = int

    x = x_min

    if num1 == 1:
        for i in range(step_c):
            d = 5*(a**2)+9*a*x-2*(x**2)
            if isclose(d, 0, rel_tol=1e-09):
                print(" Такого значения не существует... ")
            else:
                G = ((-2 * (-5 * (a ** 2) + 3 * a * x + 2 * (x ** 2))) / d)
                res.append(G)
                print("x =", x, "\tG =", G)
                x += (x_max - x_min) / (step_c - 1)
    elif num1 == 2:
        for i in range(step_c):
            d = pi*(10*(a**2)+37*a*x+7*(x**2))
            if isclose(d, 0, rel_tol=1e-09):
                print(" Такого значения не существует... ")
            else:
                F = (sin(pi * (10 * (a**2) + 37 * a * x + 7 * (x**2))) / d)
                res.append(F)
                print("x =", x, "\tF =", F)
                x += (x_max - x_min) / (step_c - 1)
    elif num1 == 3:
        for i in range(step_c):
                Y = (log(-5 * (a**2) - 16 * a * x + 16 * (x**2) + 1) / log(2))
                res.append(Y)
                print("x =", x, "\tY =", Y)
                x += (x_max - x_min) / (step_c - 1)

print("Max.res. = ", max(res))
print("Min.res. = ", min(res))
