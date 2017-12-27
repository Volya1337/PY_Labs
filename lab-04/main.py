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
    
    step = (x_max - x_min) / (step_c - 1)
    
    x = x_min

    if num1 == 1:
        while x_min <= x_max:
            d = 5*(a**2)+9*a*x_min-2*(x_min**2)
            if isclose(d, 0, rel_tol=1e-09):
                print(" Такого значения не существует... ")
            else:
                G = ((-2 * (-5 * (a ** 2) + 3 * a * x_min + 2 * (x_min ** 2))) / d)
                res.append(G)
                print("x =", x, "\tG =", G)
                x_min += step
    elif num1 == 2:
        while x_min <= x_max:
            d = pi*(10*(a**2)+37*a*x_min+7*(x_min**2))
            if isclose(d, 0, rel_tol=1e-09):
                print(" Такого значения не существует... ")
            else:
                F = (sin(pi*(10*(a**2)+37*a*x_min+7*(x_min**2))) / d)
                res.append(F)
                print("x =", x, "\tF =", F)
                x_min += step
    elif num1 == 3:
        while x_min <= x_max:
                Y = (log(-5*(a**2)-16*a*x_min+16*(x_min**2)+1) / log(2))
                res.append(Y)
                print("x =", x, "\tY =", Y)
                x_min += step

    print("Max.res. = ", max(res))
    print("Min.res. = ", min(res))
