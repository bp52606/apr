#!/usr/bin/env python3.10
from copy import copy

from Function import Function
from matplotlib import pyplot as plt
from Matrica import Matrica
from Algorithm import Algorithm
import math

#funkcija koja kreira interval od 0 do t uz korak T
def createXaxis(t, T):
    nums = []
    begin = 0.0
    while begin < t:
        begin += T
        nums.append(begin)
    return nums

#funkcija koja zbraja apsolutne razlike izmedu ocekivanih i dobivenih tocaka
def calculateX(x, xcur, t):
    x_0 = x[0, 0] * math.cos(t) + x[1, 0] * math.sin(t)
    x_1 = x[1, 0] * math.cos(t) - x[0, 0] * math.sin(t)

    return math.fabs((xcur[0, 0] - x_0)) + math.fabs((xcur[1, 0] - x_1))

#klasa koja implementira trapezni postupak
class Trapez(Algorithm):
    x: Matrica
    t: float
    f: Function
    T: float
    A: Matrica
    B: Matrica
    r: Matrica

    #inicijalizacija
    def __init__(self, x, t, T, A, B, r):
        self.x = x
        self.t = t
        self.T = T
        self.A = A
        self.B = B
        self.r = r

    # funkcija koja izvodi postupak algoritma
    def algorithm(self, f: Function, implicit=False, xprev=False, draw=True, four=False, step=30, fname="", prvi=False):
        self.f = f

        xcurr = self.x

        if prvi:
            sum = calculateX(self.x, self.x, self.t)                #racunanje razlike u tockama za prvi zadatak

        file = open(fname, "w")                                     #otvaranje datoteke u koju se upisuju rezultati
        file.write(str(xcurr) + "\n")

        x_axis = createXaxis(self.t, self.T)                        #kreiranje intervala za x os

        listzero = list()
        listone = list()

        U: Matrica = Matrica.ones(self.x.x)                         #kreiranje jedinicne matrice

        counter = 0

        for i in x_axis:
            xkeep = copy(xcurr)

            listzero.append(xkeep.matrix[0])
            listone.append(xkeep.matrix[1])

            keepR = copy(self.r)

            if four:
                self.r[0, 0] = i                                    #racunanje novih vrijednosti za r(t)
                self.r[1, 0] = i
                self.f.r = self.r
            #racunanje nove vrijednosti
            xcurr = (((U - (self.A * (self.T / 2))).__invert__() * U + (self.A * (self.T / 2))) * xkeep) \
                    + ((U - (self.A * (self.T / 2))).__invert__() * ((self.T / 2) * self.B)) * (self.r + keepR)

            file.write(str(xcurr) + "\n")

            if prvi:
                sum += calculateX(self.x, xcurr, i)

            if counter == 0 or counter == step:                     #ispisivanje svako odredene vrijednosti
                print(xcurr)
                if counter == step:
                    counter = 0
            counter += 1

        if draw:                                                    #crtanje grafova
            fig, axes = plt.subplots(2)
            axes[0].plot(x_axis, listzero)
            axes[1].plot(x_axis, listone)
            plt.show()

        rez = xcurr
        if implicit:
            rez = rez + (self.f.calculate(xcurr) + self.f.calculate(xprev)) * (self.T / 2)      #racunanje konacne vrijednosti
        file.write(str(rez))
        print(rez)
        if prvi:
            return sum, rez
        return rez
