#!/usr/bin/env python3.10
import math

from Function import Function
from Input import Input

# implementacija cetvrte ciljne funkcije
class Fourth(Function):
    inp: Input = None
    a = None
    calls = 0

    def __init__(self, a=None, inp: Input = None):
        self.inp = inp
        self.a = a

    def __call__(self, inp:Input =None,a=None):
        self.calls += 1                                                             # zabiljezi poziv funkcije
        self.inp = inp
        self.a = a
        if self.inp is not None:
            #print(self.inp.getTocke())
            x1 = self.inp.getTockaIndex(0)
            x2 = self.inp.getTockaIndex(1)

            return abs((x1-x2)*(x1+x2)) + math.sqrt(x1**2 + x2**2)                  # cetvrta funkcija
        elif self.a is not None:
            return None                                                             # jer je za vise varijabli