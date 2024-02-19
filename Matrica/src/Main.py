#!/usr/bin/env python3.10

from Matrica import Matrica

if __name__ == "__main__":

    A = Matrica("A.txt")
    B = Matrica("B.txt")
    C = Matrica()
    C.assign(A)
    3*C
    #print(~A)
    #A[0,0] = 25
    #print(C)
    C = ~A
    C += A * 0.5 * B * (A - 2 * B)
    x = C[0, 0]
    C[1, 1] = x
    D: Matrica = A
    #print(D == A)


    # LABORATORIJSKA VJEZBA

    # 1.
    print("PRVI\n")

    A = Matrica("1.txt")
    D = Matrica("1.txt")
    # ispitaj jesu li vrijednosti jendnake

    print(A[0, 0] == D[0, 0])  # true
    D[0, 0] *= 1.46566537
    D[0, 0] /= 1.46566537
    print(A[0, 0] == D[0, 0])  # false

    print(abs(A[0, 0] - D[0, 0]) < pow(10, 6))  # true

    print()

    # 2.
    print("DRUGI\n")

    M = Matrica("2.txt")
    v = Matrica("v2.txt")

    try:
        print("LU:")
        Matrica.so(M, v, 0)
    except:
        print("Pivot is zero\n")

    M = Matrica("2.txt")
    v = Matrica("v2.txt")
    try:
        print("LUP:")
        Matrica.calculate(M, v, 1)
    except:
        print("Pivot is zero\n")

    print()

    # 3.
    print("TREĆI\n")

    M = Matrica("3.txt")
    v = Matrica("v3.txt")

    try:
        print("LU:")
        Matrica.calculate(M, v, 0)
    except:
        print("Pivot is zero\n")


    M = Matrica("3.txt")
    v = Matrica("v3.txt")
    try:
        print("LUP:")
        Matrica.calculate(M, v, 1)
    except:
        print("Pivot is zero\n")

    print()

    # 4.
    print("ČETVRTI\n")

    M = Matrica("4.txt")
    v = Matrica("v4.txt")

    try:
        print("LU:")
        Matrica.calculate(M, v, 0)
    except:
        print("Pivot is zero\n")

    M = Matrica("4.txt")
    v = Matrica("v4.txt")
    try:
        print("LUP:")
        Matrica.calculate(M, v, 1)
    except:
        print("Pivot is zero\n")

    print()

    # 5.

    print("PETI\n")

    M = Matrica("5.txt")
    v = Matrica("v5.txt")

    try:
        print("LU:")
        Matrica.calculate(M, v, 0)
    except:
        print("Pivot is zero\n")

    M = Matrica("5.txt")
    v = Matrica("v5.txt")
    try:
        print("LUP:")
        Matrica.calculate(M, v, 1)
    except:
        print("Pivot is zero\n")

    print()

    # 6.

    print("ŠESTI\n")

    Matrica.epsilon = pow(10, -6)

    M = Matrica("6.txt")
    v = Matrica("v6.txt")

    try:
        print("LU:")
        Matrica.calculate(M, v, 0)
    except:
        print("Pivot is zero\n")

    M = Matrica("6.txt")
    v = Matrica("v6.txt")

    try:
        print("LU:")
        Matrica.calculate(M, v, 1)
    except:
        print("Pivot is zero\n")

    M = Matrica("6.txt")
    v = Matrica("v6.txt")

    print("Popravljanje vrijednosti matrice\n")

    M[0, 0] *= pow(10, -6)
    M[0, 1] *= pow(10, -6)
    M[0, 2] *= pow(10, -6)
    M[2, 0] *= pow(10, 6)
    M[2, 1] *= pow(10, 6)
    M[2, 2] *= pow(10, 6)
    v[0, 0] /= pow(10, 6)
    v[2, 0] *= pow(10, 6)

    try:
        print("LU:")
        Matrica.calculate(M, v, 0)
    except:
        print("Pivot is zero\n")

    M = Matrica("6.txt")
    v = Matrica("v6.txt")
    M[0, 0] *= pow(10, -6)
    M[0, 1] *= pow(10, -6)
    M[0, 2] *= pow(10, -6)
    M[2, 0] *= pow(10, 6)
    M[2, 1] *= pow(10, 6)
    M[2, 2] *= pow(10, 6)
    v[0, 0] /= pow(10, 6)
    v[2, 0] *= pow(10, 6)

    try:
        print("LUP:")
        Matrica.calculate(M, v, 1)
    except:
        print("Pivot is zero\n")

    print()

    Matrica.epsilon = pow(10,-9)

    # 7.

    print("SEDMI\n")

    M = Matrica("3.txt")
    try:
        print(~M)
    except:
        print("Matrix has no inverse")
    print()

    # 8.

    print("OSMI\n")

    M = Matrica("8.txt")
    try:
        print(~M)
    except:
        print("Matrix has no inverse")

    print()

    # 9.

    print("DEVETI\n")

    M = Matrica("8.txt")
    try:
        print(M.determinant())
    except:
        print("Matrix has no determinant")

    print()

    # 10.

    print("DESETI\n")

    M = Matrica("B.txt")
    try:
        print(M.determinant())
    except:
        print("Matrix has no determinant")

    print()