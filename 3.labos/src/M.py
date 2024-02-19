#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica

#klasa koja implementira funkciju korištenu u šestom zadatku
class M(Function):
    calls = 0
    gradcalls = 0
    hesscalls = 0
    jacobycalls = 0
    x3 = 1
    t = None
    y = None

    def __init__(self, x1=None, x2=None, t = None, y = None):
        self.x1 = x1
        self.x2 = x2
        self.t = t
        self.y = y

    def __call__(self):

        self.calls += 1

        if self.x1 is not None and self.x2 is not None:

            x1 = self.x1
            x2 = self.x2
            x3 = self.x3
            t = self.t
            y = self.y
            return x1*(math.exp(x2*t)) + x3-y

        return None

    def gradient_f(self):
        self.gradcalls+=1
        x1 = self.x1
        x2 = self.x2
        x3 = self.x3
        t = self.t
        grad = [math.exp(x2*t), x1*(math.exp(x2*t))*t, 1]

        return grad

    def hesse(self):
        self.hesscalls+=1
        mat: Matrica = Matrica(x=3, y=3)

        x1 = self.x1
        x2 = self.x2
        x3 = self.x3
        t = self.t

        mat.__setitem__([0,0], 0)
        mat.__setitem__([0,1], (math.exp(x2*t))*t)
        mat.__setitem__([0,2], 0)
        mat.__setitem__([1,0], (math.exp(x2*t))*t)
        mat.__setitem__([1,1], x1*t**2*(math.exp(x2*t)))
        mat.__setitem__([1,2], 0)
        mat.__setitem__([2, 0], 0)
        mat.__setitem__([2, 1], 0)
        mat.__setitem__([2, 2], 0)

        return mat

    def jacoby(self):
        self.jacobycalls+=1
        mat: Matrica = Matrica(x=1, y=3)

        x1 = self.x1
        x2 = self.x2
        x3 = self.x3
        t = self.t

        mat[0,0] = math.exp(x2*t)
        mat[0,1] = x1*(math.exp(x2*t))*t
        mat[0,2] = 1

        return mat

    def setx3(self, x3):
        self.x3 = x3