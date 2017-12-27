from math import log, sin, pi, isclose
# Выбор формулы #

counter = 0
res = []
res_G = []
res_F = []
res_Y = []
sres_G = ""
sres_F = ""
sres_Y = ""
common_res = []

a = float(input("Введите а: "))

x_min = str(input("Введите минимальное значение x: "))
x_min = float(x_min)

x_max = str(input("Введите макимальное значение х: "))
x_max = float(x_max)

step_c = str(input("Введите число шагов: "))
step_c = int(step_c)

x = x_min

while x <= x_max:
    d = 5*(a**2)+9*a*x_min-2*(x_min**2)
    if isclose(d, 0, rel_tol=1e-09):
        print(" Такого значения не существует... ")
        break
    else:
        G = ((-2 * (-5 * (a ** 2) + 3 * a * x + 2 * (x ** 2))) / d)
        res_G.append(res)
        print("\tG =", G)
        res_G.append(G)
        common_res.append(G)
        x += (x_max - x_min) / (step_c - 1)
        sres_G += str(G)
print("----------------------------------------------------------------")

x = x_min

while x <= x_max:
    d = pi * (10 * (a ** 2) + 37 * a * x + 7 * (x ** 2))
    if isclose(d, 0, rel_tol=1e-09):
        print(" Такого значения не существует... ")
        break
    else:
        F = (sin(pi * (10 * (a ** 2) + 37 * a * x + 7 * (x_min ** 2))) / d)
        res_F.append(res)
        print("\tF =", F)
        res_F.append(F)
        common_res.append(F)
        x += (x_max - x_min) / (step_c - 1)
        sres_F += str(F)
print("----------------------------------------------------------------")

x = x_min

while x <= x_max:
    d = (log(2))
    if isclose(d, 0, rel_tol=1e-09):
        print(" Такого значения не существует... ")
    else:
        Y = (log(-5 * (a ** 2) - 16 * a * x + 16 * (x ** 2) + 1) / log(2))
        res_Y.append(res)
        print("\tY =", Y)
        res_Y.append(Y)
        common_res.append(Y)
        x += (x_max - x_min) / (step_c - 1)
        sres_Y += str(Y)
print("----------------------------------------------------------------")
