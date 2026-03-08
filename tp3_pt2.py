# -*- coding: utf8 -*-

import math

# =====================================================
# EXERCICE 1 : Equation du second degré
# =====================================================

class EquationSecondDegre:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b**2 - 4*self.a*self.c

    def resoudre(self):
        d = self.discriminant()

        if self.a == 0:
            print("Ce n'est pas une équation du second degré.")
            return

        if d > 0:
            x1 = (-self.b - math.sqrt(d)) / (2*self.a)
            x2 = (-self.b + math.sqrt(d)) / (2*self.a)
            print("Deux solutions réelles :")
            print("x1 =", x1)
            print("x2 =", x2)

        elif d == 0:
            x = -self.b / (2*self.a)
            print("Une solution double :")
            print("x =", x)

        else:
            print("Pas de solution réelle.")


# =====================================================
# EXERCICE 2 : Classe Tableau
# =====================================================

class Tableau:

    def __init__(self):
        self.tab = []

    def Lecture(self):
        n = int(input("Nombre d'elements: "))
        for i in range(n):
            x = float(input("Element " + str(i+1) + ": "))
            self.tab.append(x)

    def Affichage(self):
        print("Tableau :", self.tab)

    def Tri_selection(self):
        t = self.tab
        n = len(t)

        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if t[j] < t[min_index]:
                    min_index = j
            t[i], t[min_index] = t[min_index], t[i]

        print("Tri par sélection :", t)

    def Tri_Insertion(self):
        t = self.tab

        for i in range(1, len(t)):
            key = t[i]
            j = i - 1
            while j >= 0 and key < t[j]:
                t[j+1] = t[j]
                j -= 1
            t[j+1] = key

        print("Tri par insertion :", t)


# =====================================================
# PROGRAMME PRINCIPAL
# =====================================================

if __name__ == '__main__':

    print("===== Equation du second degré =====")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    eq = EquationSecondDegre(a, b, c)
    eq.resoudre()


    print("\n===== Classe Tableau =====")

    t = Tableau()
    t.Lecture()
    t.Affichage()

    t.Tri_selection()
    t.Tri_Insertion()
