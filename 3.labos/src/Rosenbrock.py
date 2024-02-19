#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica


class Rosenbrock(Function):
    calls = 0
    gradcalls = 0
    hesscalls = 0
    jacobycalls = 0

    def __init__(self, x1=None, x2=None):
        self.x1 = x1
        self.x2 = x2

    def __call__(self):

        self.calls += 1

        if self.x1 is not None and self.x2 is not None:

            x1 = self.x1
            x2 = self.x2
            return (100 *((x2 - (x1 ** 2)) ** 2)) + ((1 - x1) ** 2)

        return None

    def gradient_f(self):
        self.gradcalls+=1
        x1 = self.x1
        x2 = self.x2
        grad = [(-400 * x2*x1) + -2 + (2 * x1) + (400*math.pow(x1,3)), 200 * x2 - 200 * math.pow(x1, 2)]

        return grad

    def hesse(self):
        self.hesscalls+=1
        mat: Matrica = Matrica(x=2, y=2)

        mat.__setitem__([0,0], 1200*(self.x1**2)+2-(400*self.x2))
        mat.__setitem__([0,1], (-400*self.x1))
        mat.__setitem__([1,0], -400*self.x1)
        mat.__setitem__([1,1], 200)

        return mat

    def jacoby(self):
        self.jacobycalls+=1
        mat: Matrica = Matrica(x=1, y=2)

        mat[0,0] = (-400 * self.x2*self.x1) + -2 + (2 * self.x1) + (400*math.pow(self.x1,3))
        mat[0,1] = 200 * self.x2 - 200 * math.pow(self.x1, 2)

        return mat


