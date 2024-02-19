#!/usr/bin/env python3.10
import math

from Function import Function
import Input

# implementacija prve ciljne funkcije
class Rosenbrock(Function):
    inp: Input = None
    a = None
    calls = 0

    def __init__(self, a=None, inp: Input = None):
        self.inp = inp
        self.a = a

    def __call__(self, a=None, inp: Input = None):
        self.calls += 1                             #zabiljezavanje poziva
        self.inp = inp
        self.a = a
        if self.inp is not None and len(self.inp.getTocke())>1:

            x1 = self.inp.getTockaIndex(0)
            x2 = self.inp.getTockaIndex(1)
            return (100 * ((x2 - x1 ** 2) ** 2)) + (1 - x1) ** 2        # izracun vrijednosti funkcije

        elif self.a is not None:
            return None                                                 # jer se radi o visedimenzijskoj funkciji
