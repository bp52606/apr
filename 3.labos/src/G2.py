#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica

#klasa koja implementira jednadzbu sustava linearnih jednadzbi nastalog iz Rosenbrockove funkcije
class G2(Function):
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
            return 1-x1

        return None

    def gradient_f(self):
        self.gradcalls+=1
        x1 = self.x1
        x2 = self.x2
        grad = [-1, 0]

        return grad

    def hesse(self):
        self.hesscalls+=1
        mat: Matrica = Matrica(x=2, y=2)

        mat.__setitem__([0,0], 0)
        mat.__setitem__([0,1], 0)
        mat.__setitem__([1,0], 0)
        mat.__setitem__([1,1], 0)

        return mat

    def jacoby(self):
        self.jacobycalls+=1
        mat: Matrica = Matrica(x=1, y=2)

        mat[0,0] = -1
        mat[0,1] = 0

        return mat