#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica

#klasa koja implementira cetvrtu zadanu funkciju
class Fourth(Function):
    calls = 0
    gradcalls = 0
    hesscalls = 0
    jacobycalls = 0

    def __init__(self, x1 = None, x2 = None):
        self.x1 = x1
        self.x2 = x2

    def __call__(self):

        self.calls += 1

        if self.x1 is not None and self.x2 is not None:

            x1 = self.x1
            x2 = self.x2
            return 0.25*math.pow(x1,4) - math.pow(x1,2) + 2*x1 + math.pow(x2-1,2)

        return None

    def gradient_f(self):
        self.gradcalls+=1
        x1 = self.x1
        x2 = self.x2
        grad = [math.pow(x1,3)-2*x1+2, 2*x2-2]

        return grad

    def hesse(self):
        self.hesscalls+=1
        mat: Matrica = Matrica(x=2, y=2)

        mat.__setitem__([0,0], 3*(self.x1**2)-2)
        mat.__setitem__([0,1], 0)
        mat.__setitem__([1,0], 0)
        mat.__setitem__([1,1], 2)

        return mat

    def jacoby(self):
        self.jacobycalls+=1
        mat: Matrica = Matrica(x=1, y=2)

        mat[0,0] = math.pow(self.x1,3)-2*self.x1+2
        mat[0,1] = 2*self.x2-2

        return mat