# -*-coding: utf-8 -*-

# tp2
import math
import time

print("TP2 : Time + Occurrences")

t1 = time.time()

texte = input("Entrer un texte : ")
print("Texte saisi :", texte)

nb = 0
for c in texte:
    if c == "a":
        nb += 1

print("Nombre de 'a' :", nb)

t2 = time.time()
print("Temps d'execution :", t2 - t1, "secondes")


# TP2 TRI SELECTION et TRI INSERTION
import random

def tri_selection(tab):
    t = tab.copy()
    n = len(t)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if t[j] < t[min_index]:
                min_index = j
        t[i], t[min_index] = t[min_index], t[i]
    return t

def tri_insertion(tab):
    t = tab.copy()
    for i in range(1, len(t)):
        key = t[i]
        j = i - 1
        while j >= 0 and key < t[j]:
            t[j+1] = t[j]
            j -= 1
        t[j+1] = key
    return t


print("\ncomparaison des tris ")

data = [random.randint(1,1000) for _ in range(1000)]

t1 = time.time()
tri_selection(data)
t2 = time.time()
print("Temps tri selection :", t2 - t1)

t1 = time.time()
tri_insertion(data)
t2 = time.time()
print("Temps tri insertion :", t2 - t1)


# TP3 REDIRECTION VERS FICHIER
import sys

print("\n Redirection vers fichier ")

orig_stdout = sys.stdout
f = open("output.txt", "w")
sys.stdout = f

print("Ce texte est ecrit dans le fichier.")

sys.stdout = orig_stdout
f.close()

print("Ecriture dans fichier terminee.")


# TP3 CALCUL MOYENNE DEPUIS CSV
import csv

print("\n Calcul Moyenne depuis CSV ")

with open("notes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["matiere","note_exam","note_td","coef_exam","coef_td","coef_matiere"])
    writer.writerow(["Math",14,12,2,1,3])
    writer.writerow(["Algo",16,15,2,1,2])

moyenne_generale = 0
coef_total = 0

with open("notes.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    
    for row in reader:
        note_exam = float(row[1])
        note_td = float(row[2])
        coef_exam = float(row[3])
        coef_td = float(row[4])
        coef_matiere = float(row[5])
        
        moyenne_matiere = ((note_exam*coef_exam)+(note_td*coef_td))/(coef_exam+coef_td)
        moyenne_generale += moyenne_matiere * coef_matiere
        coef_total += coef_matiere

moyenne_generale = moyenne_generale / coef_total
print("Moyenne generale :", moyenne_generale)


# TP4 GRAPHES
import numpy as np
import matplotlib.pyplot as plt

print("\n TP4 : Graphe ")

n = 1000
a = -2
b = 2

X = [a + (b-a)*k/(n-1) for k in range(n)]
Y = [x*x - 1 for x in X]

plt.plot(X, Y)
plt.title("Graphique de f(x)=x^2 - 1")
plt.legend(["f(x)=x^2 -1"])
plt.show()


n = 2000        # number of points
a = -10         # start
b = 10          # end

# Construction des abscisses
X = [a + (b - a) * k / (n - 1) for k in range(n)]

# Construction des ordonnees
Y = [
    10 * math.sin(
        (0.3 * x) * math.sin(1.3 * (x ** 2)) +
        0.00001 * (x ** 4) +
        0.2 * x +
        80
    )
    for x in X
]

# Tracé du graphe
plt.plot(X, Y, label="f(x)")
plt.title("Graphe de la fonction f(x)")
plt.legend(loc="best")
plt.show()

