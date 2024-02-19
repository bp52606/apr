#!/usr/bin/env python3.10
import math

from Function import Function
from Input import Input
from GoldenRatio import GoldenRatio
from Matrica import Matrica

import numpy as np

#implementacija Newton-Raphsonovog algoritma za trazenje minimuma funkcije
class NewtonRaphson:
    f: Function

    def __init__(self, func: Function):
        self.f = func

    def nralgorithm(self, e=math.pow(10, -6), x1=0.0, x2=0.0, golden_ratio=False, printaj = False):

        # gradijent u pocetnoj tocki


        self.f.setx1(x1)
        self.f.setx2(x2)

        grad = self.f.gradient_f()
        gradmat = Matrica(x=2, y=1)

        gradmat.__setitem__([0, 0], grad[0])
        gradmat.__setitem__([1, 0], grad[1])

        hesse: Matrica = self.f.hesse()
        step = hesse.calculate(A=hesse, v = -1*gradmat, p=True)

        stepNorm = math.sqrt(step[0, 0] ** 2 + step[1, 0] ** 2)

        min = self.f()

        divergence = 0

        keep = x1
        keep2 = x2

        while stepNorm >= e:

            if not golden_ratio:

                x1 += step[0,0]
                x2 += step[1,0]

                self.f.setx1(x1)
                self.f.setx2(x2)

                grad = self.f.gradient_f()
                gradmat: Matrica = Matrica(x=2, y=1)

                gradmat.__setitem__([0, 0], grad[0])
                gradmat.__setitem__([1, 0], grad[1])

                hesse: Matrica = self.f.hesse()
                step = hesse.calculate(A=hesse, v=-1 * gradmat, p=True)

                stepNorm = math.sqrt(step[0, 0] ** 2 + step[1, 0] ** 2)

                fun = self.f()
                if fun >= min:
                    divergence += 1

                if divergence > 10:
                    print("Divergencija!")
                    return None

                min = self.f()

                if printaj:
                    print(x1,x2)

            else:
                x = [x1, x2]
                gr = GoldenRatio(self.f)  # inicijalizacija zlatnog reza za minimizaciju u jednoj dimenziji
                inp: Input = Input()
                inp.setTocke([x1,x2])
                s =  [(step[0,0]/stepNorm), (step[1,0]/stepNorm)]
                lbd = gr.golden_ratio(inp=inp, e=e, lbd=True, x=x, e_i=np.array(s))  # racunanje zlatnog reza

                keep = x1
                keep2 = x2

                x1 += lbd * (step[0,0]/stepNorm)
                x2 += lbd * (step[1,0]/stepNorm)

                self.f.setx1(x1)
                self.f.setx2(x2)

                grad = self.f.gradient_f()
                gradmat: Matrica = Matrica(x=2, y=1)

                gradmat.__setitem__([0, 0], grad[0])
                gradmat.__setitem__([1, 0], grad[1])

                hesse: Matrica = self.f.hesse()
                step = hesse.calculate(A=hesse, v=-1 * gradmat, p=True)

                stepNorm = math.sqrt(step[0, 0] ** 2 + step[1, 0] ** 2)

                fun = self.f()
                if fun >= min:

                    divergence += 1

                if divergence > 10:

                    print("Divergencija!")

                    return None

                min = self.f()

                if printaj:
                    print(x1,x2)

        self.f.setx1(keep)
        self.f.setx2(keep2)
        return x1, x2
