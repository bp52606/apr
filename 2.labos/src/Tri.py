#!/usr/bin/env python3.10
import math

from numpy import double

from Function import Function
from Input import Input

# implementacija funkcije broj 3
class Tri(Function):
    inp: Input = None
    a = None
    calls =0

    def __init__(self, a=None, inp: Input = None):
        self.inp = inp
        self.a = a

    def __call__(self, a=None, inp: Input = None):
        self.calls+=1                               # zabiljezavanje poziva funkcije
        self.inp = inp
        self.a = a

        if self.inp is not None:
            return (self.inp.getTockaIndex(0) - 3)**2       # racunanje vrijednosti funkcije
        elif self.a is not None:

            return (self.a-3)**2                            # slucaj jednodimenzionalnog ulaza tipa float