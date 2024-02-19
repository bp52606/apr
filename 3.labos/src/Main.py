#!/usr/bin/env python3.10

from Function import Function
from Gradient import Gradient
from Third import Third
from NewtonRaphson import NewtonRaphson
from Rosenbrock import Rosenbrock
from Second import Second
from Fourth import  Fourth
from GaussNewton import GaussNewton
from G1 import G1
from G2 import G2
from G3 import G3
from G4 import G4
from G import G
from M import M
from V import V

if __name__ == "__main__":

    #1.
    print("PRVI\n")

    f: Function = Third(x1=0.0, x2=0.0)

    grad = Gradient(f)
    res = grad.gradient(x1 = 0.0, x2=0.0, golden_ratio=False)
    print("\nResult: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())

    f: Function = Third(x1=0.0, x2=0.0)

    grad = Gradient(f)
    res = grad.gradient(x1 = 0.0, x2=0.0, golden_ratio=True)
    print("\nResult: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())

    #2.
    print("\nDRUGI\n")

    f: Function = Rosenbrock(x1=-1.9, x2=2.0)

    print("Gradijent: ")

    grad = Gradient(f)
    res = grad.gradient(x1=-1.9, x2=2.0, golden_ratio=True)
    print("\nResult: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())

    f: Function = Rosenbrock(x1=-1.9, x2=2.0)

    print("\nNewton-Raphson: ")

    nr = NewtonRaphson(f)
    res = nr.nralgorithm(x1=-1.9, x2=2.0, golden_ratio=True)
    print("\nResult: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())


    f: Function = Second(x1=0.1, x2=0.3)

    print("\nGradijent: ")

    grad = Gradient(f)
    res = grad.gradient(x1=0.1, x2=0.3, golden_ratio=True)
    print("\nResult: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())

    f: Function = Second(x1=0.1, x2=0.3)

    print("\nNewton-Raphson: ")

    nr = NewtonRaphson(f)
    res = nr.nralgorithm(x1=-0.3, x2=0.3, golden_ratio=True)
    print("\nResult: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())


    #3.
    print("\nTRECI\n")

    f: Function = Fourth(x1=3.0, x2=3.0)

    print("Točka (3,3): ")

    nr = NewtonRaphson(f)
    res = nr.nralgorithm(x1=3.0, x2=3.0, golden_ratio=False)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())

    print("\nTočka (1,2): ")

    f: Function = Fourth(x1=3.0, x2=3.0)

    nr = NewtonRaphson(f)
    res = nr.nralgorithm(x1=1.0, x2=2.0, golden_ratio=False)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())

    f: Function = Fourth(x1=3.0, x2=3.0)

    print("\nTočka (3,3): ")

    nr = NewtonRaphson(f)
    res = nr.nralgorithm(x1=3.0, x2=3.0, golden_ratio=True)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())

    print("\nTočka (1,2): ")

    f: Function = Fourth(x1=3.0, x2=3.0)

    nr = NewtonRaphson(f)
    res = nr.nralgorithm(x1=1.0, x2=2.0, golden_ratio=True)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja gradijenta ", f.gradcalls)
    print("Računanja Hesseove matrice: ", f.hesscalls)
    print("Vrijednost funkcije cilja: ", f())


    #4.

    print("\nCETVRTI: \n")

    g1: Function = G1()
    g2: Function = G2()

    f: Function = Rosenbrock(x1=-1.9, x2=2.0)

    gn = GaussNewton([g1,g2])

    res = gn.gaussnewton(x1=-1.9, x2=2.0, f=f, golden_ratio=True)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja Jacobijeve matrice ", g1.jacobycalls + g2.jacobycalls)
    print("Vrijednost funkcije cilja: ", f())

    #5.

    print("\nPETI\n")

    g1: Function = G3()
    g2: Function = G4()

    f:Function = G(x1=-2.0, x2=2.0)


    gn = GaussNewton([g1, g2])
    print("(-2,2):")
    res = gn.gaussnewton(x1=-2.0, x2=2.0, f=f, golden_ratio=True)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja Jacobijeve matrice ", g1.jacobycalls + g2.jacobycalls)
    print("Vrijednost funkcije cilja: ", f())

    print("\n(2,2):")

    f: Function = G(x1=2.0, x2=2.0)

    res = gn.gaussnewton(x1=2.0, x2=2.0, f=f, golden_ratio=True)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja Jacobijeve matrice ", g1.jacobycalls + g2.jacobycalls)
    print("Vrijednost funkcije cilja: ", f())

    print("\n(2,-2):")

    f: Function = G(x1=2.0, x2=-2.0)

    res = gn.gaussnewton(x1=2.0, x2=-2.0, f=f, golden_ratio=True)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    print("Računanja Jacobijeve matrice ", g1.jacobycalls + g2.jacobycalls)
    print("Vrijednost funkcije cilja: ", f())

    #6.

    print("\nSESTI\n")

    t = [1,2,3,5,6,7]
    y = [3,4,4,5,6,8]

    fje = []

    f = V(x1=1.0, x2=1.0, x3=1.0,t=t, y=y)

    for a,b in zip(t,y):
        fje.append(M(t=a, y=b))
    gn = GaussNewton(fje)
    res = gn.gaussnewton(x1=1.0, x2=1.0, x3=1.0, f=f, golden_ratio=True)
    print("Result: ", res)
    print("Pozivi funkcije: ", f.calls)
    suma = 0
    for i in fje:
        suma+=i.jacobycalls
    print("Računanja Jacobijeve matrice ", suma)
    print("Vrijednost funkcije cilja: ", f())

