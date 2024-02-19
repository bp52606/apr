#!/usr/bin/env python3.10
import math

import numpy as np
from Function import Function
from Input import Input
import sys


def printData(xc, f):                   # ispis podataka u odredenom koraku postupka
    print("xc: ", xc, "f: ", f(xc))

# klasa koja implementira postupak optimiranja po Nelderu i Meadu
class NelderAndMead:
    f: Function = None

    def __init__(self, func: Function):
        self.f = func

    def calculateNAM(self, x0=None, e=math.pow(10,-6), pomak=1, alfa=1, beta=0.5, gamma=2, sigma=0.5, printDat=False):         # postupak optimiranja

        if x0 is None:
            x0=[]
            print("Upisi x0: ")
            inp = Input()
            for line in sys.stdin:
                if 'q' == line.rstrip(): break
                x0.append(float(line))

        simplex = list()
        simplex.append(x0)
        for i in range(len(x0)):                        # pomakni pocetne tocke za zadani pomak u svakoj dimenziji
            tocka = x0.copy()
            tocka[i] += pomak
            simplex.append(tocka)

        while True:

            inputs = list()
            for i in range(len(simplex)):
                inp = Input()
                inp.setTocke(simplex[i])
                inputs.append(inp)

            fje = np.array([self.f(inp=inputs[i]) for i in range(len(simplex))])

            h = np.argmax(fje)         # odredi index maks vrijednosti funkcije
            l = np.argmin(fje)         # odredi index min vrijednosti funkcije

            # odredivaje centroida xc
            xc = np.array([0.0] * len(x0))
            p = 0
            for k in range(len(x0) + 1):

                if k != h:
                    xc += np.array(simplex[k])
                    p += 1

            xc /= len(x0)

            inp2 = Input()
            inp2.setTocke(xc)
            fxc = self.f(inp=inp2)

            if printDat:
                printData(xc, self.f)                                                   # ispis podataka ako je tako zatrazeno

            xr = (1 + alfa) * xc - alfa * np.array(simplex[h])                          # refleksija

            inp = Input()
            inp.setTocke(xr)
            inp2 = Input()
            inp2.setTocke(simplex[l])

            fxr = self.f(inp=inp)
            fxl = fje[l]

            if fxr < fxl:
                xe = (1 - gamma) * xc + gamma * xr                                      # ekspanzija

                inp = Input()
                inp.setTocke(xe)

                fxe = self.f(inp=inp)
                if fxe < fxl:
                    simplex[h] = xe
                else:
                    simplex[h] = xr

            else:
                skup = np.array([0.0] * (len(x0)))

                p = 0
                for a in range(len(x0) + 1):
                    if a != h:
                        inp = Input()
                        inp.setTocke(simplex.copy()[a])
                        skup[p] = fje[a]
                        p += 1

                inp = Input()
                inp.setTocke(xr)
                inp2 = Input()
                inp2.setTocke(simplex[h])
                if all(fxr > skup):
                    if fxr < fje[h]:
                        simplex[h] = xr

                    xk = (1.0 - beta) * xc + beta * np.array(simplex[h])                   # kontrakcija
                    inp = Input()
                    inp.setTocke(xk)
                    fxk = self.f(inp=inp)
                    if fxk < fje[h]:
                        simplex[h] = xk
                    else:
                        for b in range(len(x0) + 1):
                            if b != l:
                                simplex[b] = sigma * (simplex[l] + simplex[b])              # pomicanje svih tocaka prema simplex[l]

                else:
                    simplex[h] = xr

            sum = 0

            for i in range(len(x0) + 1):

                sum += math.pow(fje[i] - fxc, 2)

            sum /= len(x0)
            sum = math.sqrt(sum)


            condition = sum>e                                          # ispitivanje uvjeta za prekid izvodenja postupka
            if not condition: break

        inp = Input()
        inp.setTocke(simplex[l])
        return simplex[l]
