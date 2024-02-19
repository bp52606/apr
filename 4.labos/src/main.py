#!/usr/bin/env python3.10

from Box import Box
from G1 import G1
from G2 import G2
from F4 import F4
from G5 import G5
from G6 import G6
from G7 import G7
from Rosenbrock import Rosenbrock
from Second import Second
import numpy as np
from Transform import Transform
from x import X

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #PRVI


    print("PRVI\n")

    g1 = G1()
    g2 = G2()

    limits = list()
    limits.append(g1)
    limits.append(g2)

    print("Funkcija 1:\n")

    x0 = (-1.9, 2.0)

    xd = (-100, -100)
    xg = (100, 100)

    # f = Second()
    f = Rosenbrock()
    box = Box(func=f)
    solve = box.box(x0=x0, xd=xd, xg=xg, g=limits)

    print("Rješenje: ", solve)

    print("\nFunkcija 2:\n")

    x0 = (0.1, 0.3)

    f = Second()
    box = Box(func=f)
    solve = box.box(x0=x0, xd=xd, xg=xg, g=limits)

    print("Rješenje: ", solve)

    print("\nDRUGI\n")

    print("Funkcija 1:\n")

    f = Rosenbrock()
    x0 = [-1.9, 2.0]

    transform = Transform(f)
    transform.transform(x0, g=limits)

    print("\nFunkcija 2:\n")

    f = Second()
    x0 = [0.1, 0.3]

    transform = Transform(f)
    transform.transform(x0, g=limits)

    print("\nTREĆI\n")

    x0 = [5.0, 5.0]
    g5 = G5()
    g6 = G6()
    limits = list()
    limits.append(g5)
    limits.append(g6)

    g7 = G7()

    equalities = list()
    equalities.append(g7)

    f = F4()

    transform = Transform(f)
    transform.transform(x0, g=limits)
