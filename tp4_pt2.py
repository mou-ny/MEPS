# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import math
import numpy as np

# EXo2

n = 500
a = -math.pi
b = math.pi

X = [a + (b - a) * k / (n - 1) for k in range(n)]
Y_sin = [math.sin(x) for x in X]
Y_cos = [math.cos(x) for x in X]

plt.figure()
plt.plot(X, Y_cos)
plt.plot(X, Y_sin)
plt.legend(('cos', 'sin'))
plt.title("Sin et Cos")
plt.show()


# EXo3

Lx = [k / 10 for k in range(0, 101)]   
Ly_car = [x ** 2 for x in Lx]
Ly_rac = [math.sqrt(x) for x in Lx]

plt.figure()
plt.plot(Lx, Ly_car)
plt.plot(Lx, Ly_rac)
plt.legend(('x^2', 'sqrt(x)'))
plt.title("f(x)=x^2 et g(x)=sqrt(x)")
plt.ylim(ymax=15)
plt.show()


# EXo4

x = np.linspace(0.1, 5, 100)

f = x - 1
g = np.log(x)

plt.figure()
plt.plot(x, f)
plt.plot(x, g)
plt.legend(('x-1', 'ln(x)'))
plt.title("Comparaison entre x-1 et ln(x)")
plt.savefig("graphe_exercice4.png")
plt.show()
