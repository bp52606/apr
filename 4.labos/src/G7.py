#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica

#klasa koja implementira treće zadano ograničenje u trećem zadatku
class G7(Function):
    calls = 0

    def __init__(self, x1=None, x2=None):                   #inicijalizacija funkcije
        self.x1 = x1
        self.x2 = x2

    def __call__(self, x):                                  #nadjacana metoda poziva funkcije

        self.calls += 1

        self.x2 = x[1]

        if self.x2 is not None:

            x2 = self.x2
            return x2-1

        return None

    def calculate(self, x):                     #funkcija koja racuna vrijednost za zadanu tocku x
        self.calls += 1

        self.x2 = x[1]

        if self.x2 is not None:

            x2 = self.x2
            return x2-1

        return None