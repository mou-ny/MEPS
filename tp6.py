# -*- coding: utf8 -*-

import math
import random
import matplotlib.pyplot as plt

# =====================================================
# FUNCTION TO MINIMIZE
# =====================================================

def f(x):
    return 10 * math.sin(
        (0.3 * x) *
        math.sin(1.3 * (x**2) + 0.00001 * (x**4) + 0.2 * x + 80)
    )

# =====================================================
# PARAMETERS
# =====================================================

blo = -10
bup = 10

S = 30            # number of particles
iterations = 100  # stopping condition

omega = 0.7       # inertia weight
phi_p = 1.5       # cognitive parameter
phi_g = 1.5       # social parameter
lr = 0.5          # learning rate

# =====================================================
# INITIALIZATION
# =====================================================

particles = []
velocities = []
pbest = []
pbest_val = []

# initialize particles
for i in range(S):
    
    x = random.uniform(blo, bup)
    v = random.uniform(-(bup-blo), (bup-blo))
    
    particles.append(x)
    velocities.append(v)
    
    pbest.append(x)
    pbest_val.append(f(x))

# global best
g = pbest[pbest_val.index(min(pbest_val))]

# =====================================================
# PSO MAIN LOOP
# =====================================================

for it in range(iterations):
    
    for i in range(S):
        
        rp = random.random()
        rg = random.random()
        
        # update velocity
        velocities[i] = (
            omega * velocities[i]
            + phi_p * rp * (pbest[i] - particles[i])
            + phi_g * rg * (g - particles[i])
        )
        
        # update position
        particles[i] = particles[i] + lr * velocities[i]
        
        # keep particle inside bounds
        if particles[i] < blo:
            particles[i] = blo
        if particles[i] > bup:
            particles[i] = bup
        
        # evaluate
        value = f(particles[i])
        
        # update personal best
        if value < pbest_val[i]:
            pbest[i] = particles[i]
            pbest_val[i] = value
        
        # update global best
        if value < f(g):
            g = particles[i]

# =====================================================
# RESULT
# =====================================================

print("Best solution x =", g)
print("Minimum value f(x) =", f(g))

# =====================================================
# PLOT FUNCTION AND OPTIMUM
# =====================================================

X = [blo + (bup-blo)*k/1000 for k in range(1000)]
Y = [f(x) for x in X]

plt.plot(X, Y)
plt.scatter(g, f(g))
plt.title("PSO Minimum")
plt.show()