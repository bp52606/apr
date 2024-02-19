#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica


class V(Function):
    calls = 0
    gradcalls = 0
    hesscalls = 0
    jacobycalls = 0
    x3 = 1
    t = []
    y = []

    def __init__(self, x1=None, x2=None, x3 = None, t= [], y = []):

        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    def __call__(self):

        self.calls += 1

        if self.x1 is not None and self.x2 is not None:

            x1 = self.x1
            x2 = self.x2
            x3 = self.x3
            sum = 0
            for a,b in zip(self.t, self.y):
                sum += (x1*(math.exp(x2*a)) + x3-b)**2
            return sum

        return None


    def setx3(self, x3):
        self.x3 = x3