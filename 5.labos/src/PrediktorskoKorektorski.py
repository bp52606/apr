#!/usr/bin/env python3.10
from copy import copy

from Function import Function
from Matrica import Matrica

#klasa koja implementira prediktorsko-korektorski postupak
class PrediktorskoKorektorski:
    x: Matrica
    t: float
    f: Function
    T: float
    A: Matrica
    B: Matrica
    r: Matrica

    #incijalizacija
    def __init__(self, x, t, T, A, B, r):
        self.x = x
        self.t = t
        self.T = T
        self.A = A
        self.B = B
        self.r = r

    #funkcija koja izvodi postupak algoritma
    def pred_kor(self, f: Function, iter=0, four=False, predictor=None, kontroler=None, step=30, fname="", prvi = False):

            file = open(fname, "w")     #otvaranje datoteke u koju se upisuju rezultati
            keepx = copy(self.x)

            self.f = f

            #prediktor racuna novu vrijednost
            if prvi:
                suma, xcur = predictor.algorithm(f=self.f, draw=False, four=four,fname=fname, prvi = prvi)
            else:
                xcur = predictor.algorithm(f=self.f, draw=False, four=four,fname=fname)

            file.write(str(xcur)+"\n")

            counter = 0

            #kontroler racuna nove vrijednosti
            for i in range(0, iter):
                kontroler.x = keepx
                if i == iter - 1:
                    if prvi:
                        sum, xcur = kontroler.algorithm(f=self.f, implicit=True, xprev=xcur, four=four,fname=fname, prvi = prvi)
                        suma+=sum
                    else:
                        xcur = kontroler.algorithm(f=self.f, implicit=True, xprev=xcur, four=four,fname=fname)
                else:
                    if prvi:
                        sum, xcur = kontroler.algorithm(f=self.f, implicit=True, xprev=xcur, draw=False, four=four,fname=fname, prvi = prvi)
                        suma+=sum
                    else:
                        xcur = kontroler.algorithm(f=self.f, implicit=True, xprev=xcur, draw=False, four=four,fname=fname)
                file.write(str(xcur)+"\n")

                if counter == 0 or counter == step:                 #ispisivanje svako odredene vrijednosti
                    print(xcur)
                    if counter == step:
                        counter = 0
                counter += 1

            if prvi:
                return suma, xcur
            return xcur
