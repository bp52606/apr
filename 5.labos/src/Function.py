#!/usr/bin/env python3.10

import math


# "interface" funkcije
class Function:

    x1: float = 0.0
    x2: float = 0.0

    #inciijalizacija funkcije
    def function(self, x1: float, x2: float):
        pass
    #funkcija za racunanje gradijenta
    def gradient_f(self):
        pass
    #funkcija za racunanje Hesseove matrice
    def hesse(self):
        pass

    # funkcija za racunanje Jakobijana
    def jacoby(self):
        pass

    #funkcija za racunanje norme gradijenta
    def norma(self):
        gradient = self.gradient_f()
        return math.sqrt(gradient[0] ** 2 + gradient[1] ** 2)


    #postavljanje vrijednosti x1
    def setx1(self, x1:float):
        self.x1 = x1

    #postavljanje vrijednosti x2
    def setx2(self, x2:float):
        self.x2 = x2

    #funkcija koja racuna vrijednost za zadanu tocku x
    def calculate(self, x):
        pass

    #funkcija koja nadjacava zbrajanje dvije funkcije
    def __add__(self, other):
        rez = Function()
        rez.calculate = self.calculate() + other.calculate()

