#!/usr/bin/env python3.10

import math

from Function import Function
from Input import Input
from Matrica import Matrica
from GoldenRatio import GoldenRatio
import numpy as np

#implementacija Gauss-Newtonovog algoritma za trazenje minimuma funkcije
class GaussNewton:
    f: Function = []

    def __init__(self, func: Function):
        self.f = func

    def gaussnewton(self, e=math.pow(10, -6), x1=0.0, x2=0.0, x3 = None, golden_ratio=False, f:Function= None, printaj = False):

        f.setx1(x1)
        f.setx2(x2)
        if x3 is not None:
            f.setx3(x3)

        min = f()

        divergence = 0

        if printaj:
            if x3 is not None:
                print(x1, x2, x3)
            else:
                print(x1, x2)

        keep = x1
        keep2 = x2
        keep3 = x3

        while True:


            y = 1
            x = len(self.f)
            G: Matrica = Matrica(x=x, y=y)

            y = 2
            if x3 is not None:
                y = 3
            J: Matrica = Matrica(x=x, y=y)

            for count, value in enumerate(self.f):
                value.setx1(x1)
                value.setx2(x2)
                if x3 is not None:
                    value.setx3(x3)
                G[count, 0] = value()


            for count, value in enumerate(self.f):
                value.setx1(x1)
                value.setx2(x2)
                if x3 is not None:
                    value.setx3(x3)
                J[count,0] = value.jacoby()[0,0]
                J[count,1] = value.jacoby()[0,1]
                if x3 is not None:
                    J[count, 2] = value.jacoby()[0, 2]

            A: Matrica = (J.transpose()) * J
            g: Matrica = (J.transpose()) * G
            deltaX = Matrica.calculate(A, -1*g, 1)

            lbda = 1

            if golden_ratio:
                x = [x1, x2]
                if x3 is not None:
                    x = [x1,x2,x3]
                gr = GoldenRatio(f)  # inicijalizacija zlatnog reza za minimizaciju u jednoj dimenziji
                inp: Input = Input()
                inp.setTocke([x1, x2])
                if x3 is not None:
                    inp.setTocke([x1, x2, x3])
                    lbda = gr.golden_ratio(inp=inp, e=e, lbd=True, x=np.array(x), e_i=np.array([deltaX[0,0],deltaX[1,0], deltaX[2,0]]))
                else:
                    lbda = gr.golden_ratio(inp=inp, e=e, lbd=True, x=np.array(x),
                    e_i=np.array([deltaX[0, 0], deltaX[1, 0]]))

            if (abs(deltaX[0,0] * lbda)) <= e and (abs(deltaX[1,0]* lbda) <= e):
                if x3 is not None:
                    f.setx1(keep)
                    f.setx2(keep2)
                    f.setx3(keep3)
                    return x1, x2, x3
                f.setx1(keep)
                f.setx2(keep2)
                return x1,x2

            keep = x1
            keep2 = x2

            x1 = x1 + deltaX[0, 0]
            x2 = x2 + deltaX[1, 0]
            if x3 is not None:
                x3 = x3 + deltaX[2, 0]

            f.setx1(x1)
            f.setx2(x2)
            if x3 is not None:
                f.setx3(x3)

            fun = f()

            if fun >= min:
                divergence += 1

            if divergence > 10:
                print("Divergencija!")
                f.setx1(keep)
                f.setx2(keep2)
                return None

            min = f()

            if printaj:
                if x3 is not None:
                    print(x1, x2, x3)
                else:
                    print(x1, x2)

        return None
