#!/usr/bin/env python3.10


from Rosenbrock import Rosenbrock
from GoldenRatio import GoldenRatio
from Coordinates import Coordinates
from Input import Input
from Third import Third
from NelderAndMead import NelderAndMead
from HookeJeeves import HookeJeeves
from Second import Second
from Fourth import Fourth
from Schaffer import Schaffer
from random import sample
from Tri import Tri
import math
from tabulate import tabulate
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == "__main__":

    # 1
    print("PRVI")
    print()
    function = Tri()
    gr = GoldenRatio(function)
    inp = Input()
    inp.setTocke([10.0])
    print("Golden ratio: ", gr.golden_ratio(inp=inp, e=math.pow(10,-6)))
    print("Calls: ", function.calls)
    print()

    function = Tri()
    co = Coordinates(function)
    inp = Input()
    inp.setTocke([10.0])
    print("Coordinates search: ", co.coordinates(x0=inp.getTocke(), e=pow(10, -6), n=1))
    print("Calls: ", function.calls)
    print()

    function = Tri()
    nam = NelderAndMead(function)
    inp = Input()
    inp.setTocke([10.0])
    print("Nelder and Mead: ", nam.calculateNAM(x0=inp.getTocke()))
    print("Calls: ", function.calls)
    print()

    function = Tri()
    hj = HookeJeeves(function)
    inp = Input()
    inp.setTocke([10.0])
    print("Hooke-Jeeves: ", hj.calcHookeJeeves(x0=inp.getTocke()))
    print("Calls: ", function.calls)
    print()

    # 2
    print()
    print("DRUGI")
    print()

    insides = [[-1.9,2],[0.1,0.3],[0,0,0,0,0],[5.1,1.1]]
    dicts= [{},{},{},{}]

    #dict = dicts[0]
    function = Rosenbrock()
    gco = Coordinates(function)
    inp = Input()
    inp.setTocke([-1.9, 2.0])
    dict = dicts[0]
    rez = gco.coordinates(x0=inp.getTocke(), e=pow(10, -6), n=2)
    dict["Koordinate:      "+ str(rez)] = function.calls


    function = Second()
    gco = Coordinates(function)
    inp = Input()
    inp.setTocke([0.1, 0.3])
    dict = dicts[1]
    rez = gco.coordinates(x0=inp.getTocke(), e=pow(10, -6), n=2)
    dict["Koordinate:      "+str(rez)] = function.calls

    function = Third()
    gco = Coordinates(function)
    inp = Input()
    inp.setTocke([0, 0, 0, 0, 0])
    dict = dicts[2]
    rez = gco.coordinates(x0=inp.getTocke(), e=pow(10, -6), n=5)
    dict["Koordinate:      "+str(rez)] = function.calls

    function = Fourth()
    gco = Coordinates(function)
    inp = Input()
    inp.setTocke([5.1, 1.1])
    dict = dicts[3]
    rez = gco.coordinates(x0=inp.getTocke(), e=pow(10, -6), n=2)
    dict["Koordinate:      "+str(rez)] = function.calls



    function = Rosenbrock()
    gco = NelderAndMead(function)
    inp = Input()
    inp.setTocke([-1.9, 2.0])
    dict = dicts[0]
    rez = gco.calculateNAM(x0=inp.getTocke())
    dict["Nelder and Mead: "+str(rez)] = function.calls

    function = Second()
    gco = NelderAndMead(function)
    inp = Input()
    inp.setTocke([0.1, 0.3])
    dict = dicts[1]
    rez = gco.calculateNAM(x0=inp.getTocke())
    dict["Nelder and Mead: "+str(rez)] = function.calls

    function = Third()
    gco = NelderAndMead(function)
    inp = Input()
    inp.setTocke([0, 0, 0, 0, 0])
    dict = dicts[2]
    rez = gco.calculateNAM(x0=inp.getTocke())
    dict["Nelder and Mead: "+str(rez)] = function.calls

    function = Fourth()
    gco = NelderAndMead(function)
    inp = Input()
    inp.setTocke([5.1, 1.1])
    dict = dicts[3]
    rez = gco.calculateNAM(x0=inp.getTocke())
    dict["Nelder and Mead: "+str(rez)] = function.calls

    dict = {}
    function = Rosenbrock()
    gco = HookeJeeves(function)
    inp = Input()
    inp.setTocke([-1.9, 2.0])
    dict = dicts[0]
    rez = gco.calcHookeJeeves(x0=inp.getTocke())
    dict["Hooke-Jeeves:    "+str(rez)] = function.calls

    function = Second()
    gco = HookeJeeves(function)
    inp = Input()
    inp.setTocke([0.1, 0.3])
    dict = dicts[1]
    rez = gco.calcHookeJeeves(x0=inp.getTocke())
    dict["Hooke-Jeeves:    "+str(rez)] = function.calls

    function = Third()
    gco = HookeJeeves(function)
    inp = Input()
    inp.setTocke([0.0, 0.0, 0.0, 0.0, 0.0])
    dict = dicts[2]
    rez = gco.calcHookeJeeves(x0=inp.getTocke())
    dict["Hooke-Jeeves:    "+str(rez)] = function.calls

    function = Fourth()
    gco = HookeJeeves(function)
    inp = Input()
    inp.setTocke([5.1, 1.1])
    dict = dicts[3]
    rez = gco.calcHookeJeeves(x0=inp.getTocke())
    dict["Hooke-Jeeves:    "+str(rez)] = function.calls

    for i in range(len(dicts)):
        print("Ulaz: ",insides[i])
        print()
        print(tabulate(dicts[i].items(), headers=["Output", "Calls"]))
        print()

    # 3.
    print()
    print("TRECI")
    print()

    function = Fourth()
    nam = NelderAndMead(function)
    inp = Input()
    inp.setTocke([5.0, 5.0])
    print("Nelder and Mead: ", nam.calculateNAM(x0=inp.getTocke()))
    print("Calls: ", function.calls)
    print()

    function = Fourth()
    hj = HookeJeeves(function)
    print("Hooke-Jeeves: ", hj.calcHookeJeeves(x0=inp.getTocke()))
    print("Calls: ", function.calls)
    print()

    # 4.
    print()
    print("CETVRTI")
    print()
    function = Rosenbrock()
    inp = Input()
    inp.setTocke([0.5, 0.5])
    nam = NelderAndMead(function)
    print("Tocka [0.5,0.5]")
    print()
    for i in range(1, 21):
        function = Rosenbrock()
        nam = NelderAndMead(function)
        print("Nelder and Mead: ", nam.calculateNAM(x0=inp.getTocke(), pomak=i))
        print("Calls: ", nam.f.calls)

    print()

    inp.setTocke([20.0, 20.0])
    print("Tocka [20.0,20.0]")
    print()
    for i in range(1, 21):
        function = Rosenbrock()
        nam = NelderAndMead(function)
        print("Nelder and Mead: ", nam.calculateNAM(x0=inp.getTocke(), pomak=i))
        print("Calls: ", nam.f.calls)

    print()

    # 5.
    print()
    print("PETI")
    print()
    function = Schaffer()
    inp = Input()
    sum = 0
    for i in range(1000):
        a, b = sample(range(-50, 50), 2)
        inp.setTocke([a, b])
        function = Schaffer()
        hj = HookeJeeves(function)
        rez = hj.calcHookeJeeves(x0=inp.getTocke())
        inp2 = Input()
        inp2.setTocke(rez)
        if function(inp=inp2) < math.pow(10,-4):
            sum+=1
        print("Hooke-Jeeves [", a, b, "] ", "result: ", rez)
        print("Calls: ", function.calls)
        print()

    print("Probability: ",float(sum/1000))
