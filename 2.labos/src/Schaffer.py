#!/usr/bin/env python3.10
import math

from Function import Function
from Input import Input

# implementacija Schafferove funkcije
class Schaffer(Function):
    inp: Input = None
    a = None
    calls = 0

    def __init__(self, a=None, inp: Input = None):
        self.inp = inp
        self.a = a

    def __call__(self, a=None, inp: Input = None):
        self.calls+=1                               # zabiljezavanje poziva funkcije
        self.inp = inp
        self.a = a
        if self.inp is not None:
            tocke = self.inp.getTocke()
            sum = 0
            for i in tocke:
                sum += i**2                                                 # suma kvadrata tocaka
            return 0.5+((math.sin(sum)**2 - 0.5)/((1+0.001*sum)**2))        # Schafferova funkcija
        elif self.a is not None:
            return 0.5 + ((math.sin(self.a**2) ** 2 - 0.5) / ((1 + 0.001 * self.a**2) ** 2))    # za jednodimenzionalni ulaz