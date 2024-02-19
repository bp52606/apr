#!/usr/bin/env python3.10

from Function import Function
import math
from NelderAndMead import NelderAndMead


def printData(xc, f):  # ispis podataka u odredenom koraku postupka
    print("xc: ", xc, "f: ", f(xc))


# razred koji predstavlja implementaciju postupka transformacije u problem bez ogranicenja na mjesoviti nacin
class Transform:
    f: Function

    def __init__(self, func: Function):  # inicijalizacija razreda uz definiciju funkcije koja se koristi
        self.f = func

    def transform(self, x0=None, xd=None, xg=None, e=1e-6, t=1, printDat=False, g=None,
                  h=None):  # funckija koja pronalazi tocku s najmanjom vrijedoscu zadane funkcije

        found = False  # provjera postoji li ogranicenje koje pocetna tocka ne zadovoljava
        if g is not None:
            for gi in g:
                if gi(x0) < 0:
                    found = True

        if found:  # trazenje pocetne unutarnje tocke
            findStart = Function()
            findStart.calculate = lambda x: -1 * sum(t * fun.calculate(x) for fun in g if fun.calculate(x) < 0)
            nam = NelderAndMead(findStart)
            returnDot = nam.calculateNAM(x0=x0, e=e)
            x0 = returnDot

        prev = None
        r = 1 / t
        divergence = 0
        curr = x0
        while True:


            result = Function()

            # racunanje nove funkcije cilja
            if g is not None:
                result.calculate = lambda x: self.f.calculate(x) - r * (sum(math.log(i.calculate(x)) for i in g))
            if h is not None:
                fun = Function()
                fun.calculate = lambda x: result.calculate(x) + (1 / r) * (
                    sum(math.pow(k.calculate(x, 2)) for k in h))
                result = fun

            nam = NelderAndMead(result)
            curr = nam.calculateNAM(x0=curr, e=e)     #racunanje nove vrijednosti tocke

            print(curr)


            # ispitaj uvjet zaustavljanja
            if prev is not None and all([math.sqrt(math.pow(curr[i] - prev[i], 2) + math.pow(curr[i] - prev[i], 2)) < e for i in range(len(x0))]):
                break

            if prev is None:
                prev = curr

            if result.calculate(curr) >= result.calculate(prev):
                divergence += 1

            # ispitvaj divergiranje postupka
            if divergence > 100:
                print("Divergencija!")
                break

            prev = curr

            # smanjivanje vrijednosti r
            r /= 10
