#!/usr/bin/env python3.10
from copy import copy

from Function import Function
import math
import numpy as np
import random


def printData(xc, f):  # ispis podataka u odredenom koraku postupka
    print("xc: ", xc, "f: ", f(xc))


def checkG(t=None, xr=None, x=None,
           g=None):  # funckija koja provjera zadovoljenje implicitnih ogranicenja(nejednakosti)
    for gi in g:
        if t is not None:
            if gi(x[t]) < 0: return True
        if xr is not None:
            if gi(xr) < 0: return True
    return False


def centroid(x, low, param, h):  # funkcija za racunanje centroida
    for k in range(param):
        if k != h:
            low += np.array(x[k])
    low /= param

    return low


# razred koji predstavlja implementaciju algoritma postupka po Boxu
class Box:
    f: Function

    def __init__(self, func: Function):  # inicijalizacija razreda uz definiciju funkcije koja se koristi
        self.f = func

    def box(self, x0=None, xd=None, xg=None, e=1e-6, alfa=1.3, printDat=False,
            g=None):  # funckija koja pronalazi tocku s najmanjom vrijedoscu zadane funkcije

        # provjera zadovoljenja donje granice
        for i, j in enumerate(xd):
            if x0[i] < j:
                print("Error in start values!")
                return None
        # provjera zadovoljenja gornje granice
        for i, j in enumerate(xg):
            if x0[i] > j:
                print("Error in start values!")
                return None
        # provjera zadovoljenja implicitnih ogranicenja
        for gi in g:
            if gi(x0) < 0:
                print("Error in start values!")
                return None

        n = len(x0)  # inicijalizacija varijable n

        xc = x0

        x = list()  # lista tocaka

        for t in range(2 * n):
            dot = np.zeros(shape=n)
            for i in range(n):
                # kreiranje tocaka
                R = random.uniform(0, 1)
                dot[i] = xd[i] + R * (xg[i] - xd[i])

            x.append(dot)

            fix = 0

            # provjera zadovoljavaju li nove tocke implicitna ogranicenja
            while checkG(t=t, x=x, g=g) and fix < 100:
                fix += 1
                x[t] = 0.5 * (x[t] + xc)

            fje = np.array([self.f(x[i]) for i in range(t + 1)])
            # pronalazenje indeksa najbolje i najgore tocke
            h = np.argmax(fje)
            l = np.argmin(fje)

            xc = centroid(x=x, low=copy(x[l]), param=t + 1, h=h)  # racunanje centroida

        min = self.f(x[l])
        divergence = 0

        # ponavljaj
        while True:

            fje = np.array([self.f(x[i]) for i in range(2 * n)])

            h = np.argmax(fje)  # odredi index maks vrijednosti funkcije

            minn = fje[np.argmin(fje)]

            rez = 0
            for ind, el in enumerate(fje):  # pronalazak druge najgore tocke
                if fje[ind] > minn and ind != h:
                    minn = fje[ind]
                    rez = ind

            h2 = rez

            # print(fje, h2)

            xc = centroid(x=x, low=copy(x[l]), param=len(x), h=h)  # racunanje centroida bez najgore tocke

            xr = (1 + alfa) * xc - alfa * x[h]  # refleksija

            for i in range(n):  # provjeri zadana eksplicitna ogranicenja
                if xr[i] < xd[i]:
                    xr[i] = xd[i]
                elif xr[i] > xg[i]:
                    xr[i] = xg[i]

            fix = 0
            while checkG(xr=xr, x=x, g=g) and fix < 100:  # provjeri zadana implicitna ogranicenja
                fix += 1
                xr = 0.5 * (xr + xc)

            if self.f(xr) > self.f(x[h2]):  # ako je jos uvijek najgora tocka, pomakni opet prema centroidu
                xr = 0.5 * (xr + xc)

            x[h] = xr

            fje = np.array([self.f(x[i]) for i in range(2 * n)])
            l = np.argmin(fje)

            fxc = self.f(xc)

            # provjeri uvjet zaustavljanja postupka
            sum = 0

            for i in range(len(x)):
                sum += math.pow(fje[i] - fxc, 2)

            sum /= len(x)
            sum = math.sqrt(sum)

            condition = sum > e  # ispitivanje uvjeta za prekid izvodenja postupka
            if not condition:
                break

            # provjeri divergira li postupak

            fun = self.f(x[l])

            if fun >= min:
                divergence += 1

            if divergence > 100:
                print("Divergencija!")

                break

            min = self.f(x[l])

        return x[l]  # vrati najbolju tocku
