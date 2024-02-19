#!/usr/bin/env python3.10

import math

import numpy as np
from Function import Function
from Input import Input
import sys


def printData(xb, x0, xn, f):  # ispis podataka u koracima postupka
    inp = Input()
    inp.setTocke(xb)
    print("xb: ", xb, "f(xb): ", f(inp=inp))
    inp.setTocke(x0)
    print("x0: ", x0, "f(x0): ", f(inp=inp))
    inp.setTocke(xn)
    print("xn: ", xn, "f(xn): ", f(inp=inp))


# klasa koja implementira Hooke-Jeeves postupak optimiranja
class HookeJeeves:

    def __init__(self, func: Function):  # inicijalizacija koristene ciljne funkcije
        self.f = func

    def calcHookeJeeves(self, dx=None, e=None, x0=None, printDat=False):  # postupak optimiranja
        # print(x0)
        if x0 is None:
            x0=[]
            print("Upisi x0: ")
            inp = Input()
            for line in sys.stdin:
                if 'q' == line.rstrip(): break
                x0.append(float(line))


        xp = np.array(x0.copy())
        xb = np.array(x0.copy())
        if dx is None:  # u slucaju da vektor pomaka dx nije zadan, sve mu se vrijednosti postavljaju na 0.5
            dx = []
            for l in range(len(x0)):
                dx.append(0.5)
        if e is None:  # u slucaju da vektor granicne preciznosti e nije zadan, sve mu se vrijednosti postavljaju na 1e-6
            e = []
            for l in range(len(x0)):
                e.append(math.pow(10, -6))
        while True:

            xn = self.istrazi(xp, dx)  # potprogram definiran

            if printDat:  # ispis podataka ako je tako zatrazeno
                printData(xb, x0, xn, self.f)

            inp = Input()
            inp.setTocke(xn)
            inp2 = Input()
            inp2.setTocke(xb)

            if self.f(inp=inp) < self.f(inp=inp2):  # prihvacanje bazne tocke
                xp = 2 * xn - xb  # definiranje nove tocke pretrazivanja
                xb = xn

            else:
                dx = np.array(dx) / 2
                xp = xb  # vracanje na zadnju baznu tocku

            condition = all(np.array(dx) >= e)
            if not condition: break
        return xb

    def istrazi(self, xp, dx):  # definirani potprogram

        x = xp.copy()

        for i in range(len(x)):
            inp = Input()
            inp.setTocke(x)
            P = self.f(inp=inp)

            x[i] += dx[0]  # povecanje elemenata vektora x za vrijednost pomaka dx

            inp = Input()
            inp.setTocke(x)
            N = self.f(inp=inp)

            if N > P:  # pozitivan pomak nije dobar
                x[i] = x[i] - 2 * np.array(dx[0])  # smanjenje za pomak dx
                inp = Input()
                inp.setTocke(x)
                N = self.f(inp=inp)
                if N > P:  # ako ni negativan pomak nije dobar
                    x[i] += dx[0]  # vrati na pocetnu vrijednost

        return x
