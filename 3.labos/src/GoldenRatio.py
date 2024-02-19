#!/usr/bin/env python3.10
import math
import sys
import numpy as np

from Function import Function
from Input import Input

# ispis potrebnih podataka
def printData(a, b, c, d,f,lbd,x,e_i):
    if not lbd:
        print("a: ", a, "fa: ", f(a))
        print("b: ", b, "fb: ", f(b))
        print("c: ", c, "fc: ", f(c))
        print("d: ", d, "fd: ", f(d))
    else:
        print("a: ", a, "fa: ", f(x+a*e_i))
        print("b: ", b, "fb: ", f(x+b*e_i))
        print("c: ", c, "fc: ", f(x+c*e_i))
        print("d: ", d, "fd: ", f(x+d*e_i))

# klasa koja implementira postupak optimiranja koristeci zlatni rez
class GoldenRatio:
    k = 0.5 * (math.sqrt(5) - 1)
    f: Function

    def __init__(self, func: Function):
        self.f = func

    def golden_ratio(self, inp: Input= None, e=None, lbd=False, x=None, e_i=None, printDat = False):

        xs = []
        if inp is None:
            print("Upisi x: ")
            inp = Input()
            for line in sys.stdin:
                if 'q' == line.rstrip(): break
                xs.append(float(line))
            inp.setTocke(tocke=np.array(xs))

        if e is None:
            print("Upisi e: ")
            for line in sys.stdin:
                e = float(line)
                break

        a = inp.getA()
        b = inp.getB()
        inpu = Input()

        if a is None or b is None:              # u slucaju da unimodalni interval nije definiran, njegovo trazenje

            a, b = self.unimodalni(h=1, tocka=inp.getTockaIndex(0), lbd=lbd, x=x, e_i=e_i)

        c = b - self.k * (b - a)                #odredivanje tocke c
        d = a + self.k * (b - a)                #odredivanje tocke d

        # racunanje vrijednosti ciljnih funkcija u tockama c i d
        if lbd:
            self.f.setx1(x[0] + c * e_i[0])
            self.f.setx2(x[1] + c * e_i[1])
            fc = self.f()
            self.f.setx1(x[0] + d * e_i[0])
            self.f.setx2(x[1] + d * e_i[1])
            fd = self.f()
        else:
            fc = self.f(c)
            fd = self.f(d)

        while (b - a) > e:

            if printDat:                       # ispis podataka ako je tako zadano
                printData(a,b,c,d,self.f,lbd,x,e_i)

            if fc < fd:                         # ako je vrijednost funckije u tocki c manja nego vrijednost funkcije u tocki d
                b = d
                d = c
                c = b - self.k * (b - a)
                fd = fc

                # racunanje vrijednosti funkcije u tocki c
                if lbd:
                    self.f.setx1(x[0] + c * e_i[0])
                    self.f.setx2(x[1] + c * e_i[1])
                    fc = self.f()
                else:
                    fc = self.f(c)

            else:                               #inace
                a = c
                c = d
                d = a + self.k * (b - a)
                fc = fd
                # racunanje vrijednosti funkcije u tocki d
                if lbd:
                    self.f.setx1(x[0] + d * e_i[0])
                    self.f.setx2(x[1] + d * e_i[1])
                    fd = self.f()
                else:
                    fd = self.f(d)

        input2 = Input()
        input2.setTocke([(a + b) / 2])

        if lbd:
            input2.setTocke(x + (((a + b) / 2) * e_i))

        return (a+b)/2

    def unimodalni(self, h, tocka, lbd=False, x=None, e_i=None):                # funkcija za trazenje unimodalnog intervala

        # racunanje tocaka l, r i m

        l = tocka - h
        r = tocka + h
        m = tocka
        step = 1
        inp = Input()

        # racunanje vrijednosti funkcija u tockama l,r i m
        if lbd:
            #print(x, "e_i:", e_i)
            self.f.setx1(x[0] + tocka * e_i[0])
            self.f.setx2(x[1] + tocka * e_i[1])

            fm = self.f()

            self.f.setx1(x[0] + l * e_i[0])
            self.f.setx2(x[1] + l * e_i[1])
            fl = self. f()

            self.f.setx1(x[0] + r * e_i[0])
            self.f.setx2(x[1] + r * e_i[1])
            fr = self.f()

        else:
            fm = self.f(tocka)
            fl = self.f(l)
            fr = self.f(r)

        if fm < fr and fm < fl:             # slucaj kada se prekida izvodenje trazenja
            return l,r;
        elif fm > fr:                       # slucaj da je vrijednost funkcije u tocki m veca nego vrijednost funkcije u tocki r

            while True:
                l = m
                m = r
                fm = fr

                # povecanje koraka

                step *= 2

                # racunanje vrijednosti u tocki r

                r = tocka + h * step
                # racunanje vrijednosti funkcije u tocki r
                if lbd:
                    self.f.setx1(x[0] + r * e_i[0])
                    self.f.setx2(x[1] + r * e_i[1])
                    fr = self.f()
                else:
                    fr = self.f(r)
                if fm <= fr:        # ispitivanje uvjeta za prekid petlje
                    break

        else:
            while True:
                r = m
                m = l
                fm = fl
                # povecanje koraka
                step *= 2
                # racunanje vrijednosti u tocki l
                l = tocka - h * step
                # racunanje vrijednosti funkcije u tocki l
                if lbd:
                    self.f.setx1(x[0] + l * e_i[0])
                    self.f.setx2(x[1] + l * e_i[1])
                    fl = self.f()

                else:
                    fl = self.f(l)
                if fm <= fl:            # ispitivanje uvjeta za prekid petlje
                    break

        return l, r

