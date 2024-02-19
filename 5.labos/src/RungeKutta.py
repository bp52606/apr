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

#klasa koja implementira postupak Runge-Kutta
class RungeKutta(Algorithm):
    x: Matrica
    t: float
    f: Function
    T: float
    r: Matrica

    #inicijalizacija
    def __init__(self, x, t, T, A, B, r):
        self.x = x
        self.t = t
        self.T = T
        self.r = r

    # funkcija koja izvodi postupak algoritma
    def algorithm(self, f: Function, implicit=False, four=False, step=30, fname="", prvi=False):
        self.f = f

        xcurr = self.x

        if prvi:
            sum = calculateX(self.x, self.x, self.t)         #racunanje razlike u tockama za prvi zadatak

        file = open(fname, "w")         #otvaranje datoteke u koju se upisuju rezultati
        file.write(str(xcurr) + "\n")

        x_axis = createXaxis(self.t, self.T)        #kreiranje intervala za x os

        listzero = list()
        listone = list()

        counter = 0

        for i in x_axis:

            if four:
                self.f.r[0, 0] = i              #racunanje nove vrijednosti za r(t)
                self.f.r[1, 0] = i
            # self.f.r.printMatrix()
            m1 = self.f.calculate(xcurr)
            if four:
                self.f.r[0, 0] = i + self.T / 2
                self.f.r[1, 0] = i + self.T / 2
            m2 = self.f.calculate(xcurr + self.T / 2 * m1)
            if four:
                self.f.r[0, 0] = i + self.T / 2
                self.f.r[1, 0] = i + self.T / 2
            m3 = self.f.calculate(xcurr + self.T / 2 * m2)
            if four:
                self.f.r[0, 0] = i + self.T
                self.f.r[1, 0] = i + self.T
            m4 = self.f.calculate(xcurr + self.T * m3)
            xkeep = copy(xcurr)
            listzero.append(xkeep.matrix[0])
            listone.append(xkeep.matrix[1])
            xcurr = xkeep + (self.T / 6) * (m1 + 2 * m2 + 2 * m3 + m4)      #racunanje iznosa nove vrijednosti

            if prvi:
                sum += calculateX(self.x, xcurr, i)                         #racunanje razlike izmedu vrijednosti za prvi zadatak

            file.write(str(xcurr) + "\n")

            if counter == 0 or counter == step:                             #ispisivanje svako odredene vrijednosti
                print(xcurr)
                if counter == step:
                    counter = 0
            counter += 1

        #crtanje grafova
        fig, axes = plt.subplots(2)

        axes[0].plot(x_axis, listzero)
        axes[1].plot(x_axis, listone)
        plt.show()

        if prvi:
            return sum, xcurr
        return xcurr
