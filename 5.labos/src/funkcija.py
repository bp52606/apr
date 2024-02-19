#!/usr/bin/env python3.10
import math

from Function import Function
from Matrica import Matrica

#implementacije zadane funkcije
class funkcija(Function):
    calls = 0
    A:Matrica
    B:Matrica
    x:Matrica
    r: Matrica

    def __init__(self, x=None,A=None,B=None,r=None):      #inicijalizacija funkcije
        self.x = x
        self.A = A
        self.B = B
        self.r = r

    def calculate(self, x):                 #funkcija koja racuna vrijednost za zadanu tocku x
        self.calls += 1
        if self.B is not None:
            return self.A*x + self.B*self.r
        else:
            return self.A*x
