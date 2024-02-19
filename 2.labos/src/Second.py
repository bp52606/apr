#!/usr/bin/env python3.10
import math

from Function import Function
from Input import Input

# implementacija druge ciljne funkcije
class Second(Function):
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
            x1 = self.inp.getTockaIndex(0)
            x2 = self.inp.getTockaIndex(1)
            return (x1-4)**2 + 4*((x2-2)**2)        # druga funkcija
        elif self.a is not None:
            return None                             # jer je funkcija vise varijabli