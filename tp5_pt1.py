# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import math
import random
import numpy as np

# def

def f(x):
    return 10 * math.sin(
        (0.3 * x) *
        math.sin(1.3 * (x ** 2) + 0.00001 * (x ** 4) + 0.2 * x + 80)
    )


# plot

a = 0
b = 10
n = 2000

X = [a + (b - a) * k / (n - 1) for k in range(n)]
Y = [f(x) for x in X]

plt.figure()
plt.plot(X, Y)
plt.title("Graphe de f(x)")
plt.show()


# simulate

def recuit_simule():
    
    
    T = 80        
    N = 100       
    h = 0.80      
    
    
    S = random.uniform(a, b)
    
    while T > 0:

        accepted = False
        
        for i in range(N):
            
            # new sol
            S1 = S + random.uniform(-1, 1)
            
            # keep int
            if S1 < a:
                S1 = a
            if S1 > b:
                S1 = b
            
            dF = f(S1) - f(S)
            
            if dF < 0:
                S = S1
                accepted = True
            else:
                if random.random() < math.exp(-dF / T):
                    S = S1
                    accepted = True
        
        if not accepted:
            print("stop mate")
            break
        # Cooling
        T = h * T
        
        if T < 1e-6:
            break
    
    return S


# Run opt
best_x = recuit_simule()
best_y = f(best_x)

print("Solution optimale approx x =", best_x)
print("Valeur minimale approx f(x) =", best_y)


# graph

plt.figure()
plt.plot(X, Y)
plt.scatter(best_x, best_y)
plt.title("Minimum trouvé par Recuit Simulé")
plt.show()
