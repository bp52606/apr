#!/usr/bin/env python3.10
import math

from numpy import double

from Function import Function
from Input import Input

# implementacija trece funkcije
class Third(Function):
    inp: Input = None
    a = None
    calls = 0

    def __init__(self, a=None, inp: Input = None):
        self.inp = inp
        self.a = a

    def __call__(self, a=None, inp: Input = None):
        self.calls+=1                           # zabiljezavanje poziva funkcije
        self.inp = inp
        self.a = a

        if self.inp is not None:
            tocke = self.inp.getTocke()
            sum = 0
            for i in range(len(tocke)):
                sum += (self.inp.getTockaIndex(i) - (i+1))**2       # treca funkcija

            return sum
        elif self.a is not None:

            return (self.a-1)**2                                    # slucaj jednodimenzionalnog ulaza