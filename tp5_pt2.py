# -*- coding: utf8 -*-

import math
import random
import matplotlib.pyplot as plt



# GRAPH EXAMPLE

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 3, 'B': 2, 'D': 7},
    'D': {'B': 5, 'C': 7}
}

start = 'A'
end = 'D'


# cost fun
def path_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]
    return cost


# GENERATE RANDOM PATH

def random_path():
    nodes = list(graph.keys())
    nodes.remove(start)
    nodes.remove(end)
    random.shuffle(nodes)
    return [start] + nodes + [end]


# SIMULATED ANNEALING FOR PATH

def recuit_path():

    T = 80
    N = 100
    h = 0.80

    S = random_path()
    best = S[:]

    while T > 0:

        for i in range(N):

            S1 = S[:]
            
            # swap two intermediate nodes
            i1 = random.randint(1, len(S1)-2)
            i2 = random.randint(1, len(S1)-2)
            S1[i1], S1[i2] = S1[i2], S1[i1]

            dF = path_cost(S1) - path_cost(S)

            if dF < 0 or random.random() < math.exp(-dF/T):
                S = S1[:]

            if path_cost(S) < path_cost(best):
                best = S[:]

        T = h * T

    return best


best_path = recuit_path()
print("Meilleur chemin trouvé :", best_path)
print("Cout :", path_cost(best_path))
