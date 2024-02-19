#!/usr/bin/env python3.10

from Function import Function
import numpy as np
from GoldenRatio import GoldenRatio
from Input import Input
import sys


# klasa koja implementira računanje minimuma pretraživanjem po koordinatnim osima
class Coordinates:
    f: Function = None

    # inicijalizacija funkcije cilja korištene pri računanju
    def __init__(self, func: Function):
        self.f = func

    def coordinates(self, x0=None, e=None, n=None):


        if x0 is None:
            x0=[]
            print("Upisi x0: ")
            inp = Input()
            for line in sys.stdin:
                if 'q' == line.rstrip(): break
                x0.append(float(line))
                #x0 = np.array(x0)

        if e is None:
            print("Upisi e: ")
            for line in sys.stdin:
                e = float(line)
                break

        x = x0

        while True:
            xs = x.copy()
            for i in range(0, n):
                e_i = np.array([0.0] * n)
                e_i[i] = 1
                # print(e_i)
                gr = GoldenRatio(self.f)        # inicijalizacija zlatnog reza za minimizaciju u jednoj dimenziji
                inp: Input = Input()
                inp.setTocke([xs[i]])
                lbd = gr.golden_ratio(inp, e, lbd=True, x=x, e_i=e_i)       # racunanje zlatnog reza
                # print(lbd)

                x += lbd * e_i

            condition = abs(x - xs) > e       # uvjet koji mora biti zadovoljen za x i xs vektore, inace se prekida petlja

            if not all(condition):
                break

        return x
