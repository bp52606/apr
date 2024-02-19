#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica

#klasa koja implementira funkciju rastavljenu na sustav linearnih jednadzbi(5. zadatak)
class G(Function):
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
            return ((x1**2) + (x2**2)-1)**2 + (x2 - (x1**2))**2

        return None
