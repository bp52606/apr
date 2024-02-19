#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica


# klasa koja implementira drugu zadanu funkciju
class Second(Function):
    calls = 0

    def __init__(self, x1=None, x2=None):           #inicijalizacija funkcije
        self.x1 = x1
        self.x2 = x2

    def __call__(self, x):                          #nadjacana metoda poziva funkcije
        self.calls += 1

        self.x1 = x[0]
        self.x2 = x[1]

        x1 = self.x1
        x2 = self.x2
        return math.pow(x1 - 4, 2) + 4 * math.pow(x2 - 2, 2)

    def calculate(self, x):                         #funkcija koja racuna vrijednost za zadanu tocku x
        self.calls += 1

        self.x1 = x[0]
        self.x2 = x[1]

        x1 = self.x1
        x2 = self.x2
        return math.pow(x1 - 4, 2) + 4 * math.pow(x2 - 2, 2)
