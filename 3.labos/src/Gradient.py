#!/usr/bin/env python3.10
import math

from Function import Function
from Input import Input
from GoldenRatio import GoldenRatio
import numpy as np

#implementacija gradijentnog algoritma za trazenje minimuma funkcije
class Gradient:
    f: Function

    def __init__(self, func: Function):
        self.f = func

    def gradient(self, e=math.pow(10, -6), x1=0.0, x2=0.0, golden_ratio=False, printaj = False):

        self.f.setx1(x1)
        self.f.setx2(x2)

        divergence = 0

        g1 = self.f.gradient_f()[0]
        g2 = self.f.gradient_f()[1]

        v1 = - g1
        v2 = - g2

        keep = x1
        keep2 = x2

        min = self.f()

        if printaj:
            print(x1, x2)

        if not golden_ratio:

            while math.sqrt(g1 ** 2 + g2 ** 2) >= e:
                keep = x1
                keep2 = x2
                x1 -= g1
                x2 -= g2

                self.f.setx1(x1)
                self.f.setx2(x2)

                g1 = self.f.gradient_f()[0]
                g2 = self.f.gradient_f()[1]

                fun = self.f()

                if fun >= min:
                    divergence += 1

                if divergence > 10:
                    print("Divergencija!")
                    return None

                min = self.f()

                if printaj:
                    print(x1, x2)

        else:

            v1 = v1 / self.f.norma()
            v2 = v2 / self.f.norma()
            v = [v1, v2]



            while math.sqrt(g1 ** 2 + g2 ** 2) >= e:

                x = [x1, x2]
                gr = GoldenRatio(self.f)  # inicijalizacija zlatnog reza za minimizaciju u jednoj dimenziji
                inp: Input = Input()
                inp.setTocke([x1, x2])
                lbd = gr.golden_ratio(inp=inp, e=e, lbd=True, x=x, e_i=np.array(v))  # racunanje zlatnog reza


                keep = x1
                keep2 = x2

                x1 += lbd * v1
                x2 += lbd * v2

                self.f.setx1(x1)
                self.f.setx2(x2)

                g1 = self.f.gradient_f()[0]
                g2 = self.f.gradient_f()[1]

                v1 = - g1 / self.f.norma()
                v2 = - g2 / self.f.norma()

                v = [v1, v2]

                fun = self.f()

                if fun >= min:
                    divergence += 1

                if divergence > 10:
                    print("Divergencija!")

                    return None

                min = self.f()

                if printaj:
                    print(x1, x2)

        self.f.setx1(keep)
        self.f.setx2(keep2)
        return x1, x2
