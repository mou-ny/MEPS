# -*-coding: utf-8 -*-
# q1

i = 0
s = 0
c = "a"
print("i =", i, " s =", s, " c =", c)


# q2
print("a", 2, 3, "\n", 5)

c = input("Donne c: ")
print("Vous avez saisi:", c)


# q3
s = 0
i = 1
while i <= 100:
    s = s + i
    i = i + 1
print("Somme avec while =", s)

s = 0
for i in range(1, 101):
    s = s + i
print("Somme avec for =", s)


# q4
liste6 = []

print("\nEntrez 6 elements :")
for i in range(6):
    x = input("Element " + str(i+1) + ": ")
    liste6.append(x)

print("Longueur de la liste :", len(liste6))

indice = int(input("Indice a remplacer (0-5): "))
nouvelle_valeur = input("Nouvelle valeur: ")
liste6[indice] = nouvelle_valeur

indice_sup = int(input("Indice a supprimer: "))
del(liste6[indice_sup])

valeur_ajout = input("Valeur a ajouter: ")
liste6.append(valeur_ajout)

print("Liste modifiée :", liste6)

print("Elements un par un:")
for element in liste6:
    print(element)



# q5

import random

notes = []
print("Saisir 10 notes :")
for i in range(10):
    n = float(input("Note " + str(i+1) + ": "))
    notes.append(n)

print("Une note au hasard :", random.choice(notes))

print("Liste avant melange :", notes)

random.shuffle(notes)

print("Liste apres melange :", notes)
