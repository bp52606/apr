#!/usr/bin/env python3.10

# ulazne vrijednosti za optimizaciju, tocka ili niz tocaka, interval
class Input:

    a = None            # donja granica intervala
    b = None            # gornja granica intervala

    tocke = []          # ulazne tocke

    def setA(self,a):           # postavljanje donje granice intervala
        self.a = a

    def getA(self):             # dohvacanje donje granice intervala
        return self.a

    def setB(self, b):          # postavljanje gornje granice intervala
        self.b = b

    def getB(self):             # dohvacanje gornje granice intervala
        return self.b

    def setTocke(self, tocke:list):     # postavljanje niza ulaznih tocaka
        self.tocke = tocke

    def getTocke(self):                 # dohvacanje ulaznih tocaka
        return self.tocke

    def getTockaIndex(self,index):      # dohvacanje ulazne tocke na odredenom indexu u listi
        return self.tocke[index]


