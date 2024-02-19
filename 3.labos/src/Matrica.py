#!/usr/bin/env python3.10

import numpy as np

class Matrica:
    x = 0
    y = 0

    matrix = np.array([])

    pathToFile = ""

    epsilon = 1e-9

    def __init__(self, pathToFile=None, x=None,
                 y=None):  # konstruktor koji prima ime putanje do datoteke sa podacima o matrici te broj redaka i stupaca

        if x is not None and y is not None:  # ako su zadani x i y, poszavi dimenzije matrici
            self.x = x
            self.y = y

        if pathToFile is not None:  # ako je zadana putanja, postavi je
            self.pathToFile = pathToFile

        self.createMatrix()

    def createMatrix(self):

        if self.pathToFile != "":  # u slucaju da je zadan file sa podacima

            with open(self.pathToFile) as file:

                redak = 0
                lines = file.readlines()  # procitaj zapisane podatke
                self.x = len(lines)
                for line in lines:

                    elementi = line.strip().split(" ")  # vraca listu brojeva zapisanih u datoteci

                    if self.y == 0:
                        self.y = len(elementi)  # ako jos nije postavljen, postavi y
                        self.matrix = [[0] * self.y for row in
                                       range(self.x)]  # inicijaliziraj praznu matricu sada poznatih dimenzija

                    for j in range(0, self.y):
                        self.matrix[redak][j] = float(elementi[j])  # ubacuj elemente u matricu

                    redak += 1

        elif self.x != 0 and self.y != 0:  # u slucaju da datoteka nije zadana, no dimenzije jesu

            self.matrix = [[0] * self.y for row in range(self.x)]  # inicijaliziraj praznu matricu

    def storeElements(self, elements):  # pospremi elemente u novu datoteku, vrati je

        file = open("mystorefFile.txt", "x")

        for i in range(len(elements)):
            line = ""
            for j in range(len(elements[i])):
                line += elements[i][j] + " "  # spajaj elemente retka u jedan string

            file.write(line)  # zapisi redak u datoteku

        return file

    def printMatrix(self):  # printanje matrice
        for i in range(0, self.x):
            for j in range(0, self.y):
                print(self.matrix[i][j], end="")

            if i < self.x - 1:
                print()

    def __getitem__(self, item):  # overloadano dohvacanje elementa matrice
        x, y = item
        return self.matrix[x][y]

    def __setitem__(self, key, value):  # overloadano postavljanje elementa matrice
        x, y = key
        self.matrix[x][y] = value

    def __iadd__(self, other):  # overloadano zbrajanje matrica, npr. A+=B
        return self + other

    def __invert__(self):  # računanje inverza matrice
        savex = self.x
        savey = self.y
        P, suma, L, U = self.decomposition(
            p=True)  # Jedinična matrica sa izmijenjenim retcima s obzirom na biranje pivota u LUP dekompoziciji
        E = Matrica(x=savex, y=1)  # vektor s nulama, dimenzije self.x X 1

        rez = Matrica(x=savex, y=savey)  # matrica u koju se sprema inverz

        # self.x iteracija supstitucija unaprijed i unatrag
        for i in range(0, savex):
            E[i, 0] = 1  # postavi odgovarajući element vektora u jedinicu
            if i > 0:
                E[i - 1, 0] = 0  # vrati prethodno stavljenu jedinicu u nulu

            y = self.forwardSubstitution(P * E)  # supstitucija unaprijed
            x = self.backwardSubstitution(y)  # supstitucija unatrag
            # print(x)

            for j in range(0, x.x):
                rez[j, i] = x[j, 0]  # stavi dobivene elemente stupca x u matricu inverza

        return rez

    def __isub__(self, other):  # overloadano oduzimanje matrica, npr. A-=B
        return self - other

    def __imul__(self, other):  # overloadano mnozenje matrica, npr. A *= B
        return self * other

    def __add__(self, other):  # zbrajanje matrica, npr. A+B ili A+3
        ret = Matrica(x=self.x, y=self.y)
        if isinstance(other, Matrica):  # provjera jesu li oba objekta matrice
            if self.x == other.x and self.y == other.y:  # provjera jednakosti dimenzija matrica
                for i in range(0, self.x):
                    for j in range(0, self.y):
                        ret[i, j] = self.matrix[i][j] + other.matrix[i][j]
            else:
                raise "Matrice nisu istih dimenzija."

        else:  # u slucaju da se matricu zbraja sa skalarom
            for i in range(0, self.x):
                for j in range(0, self.y):
                    ret[i, j] = self.matrix[i][j] + other

        return ret

    def __sub__(self, other):  # overloadano oduzimanje matrica, npr. A-B ili A-3
        ret = Matrica(x=self.x, y=self.y)
        if isinstance(other, Matrica):  # provjera tipa objekta
            if self.x == other.x and self.y == other.y:
                for i in range(0, self.x):
                    for j in range(0, self.y):
                        ret[i, j] = self.matrix[i][j] - other.matrix[i][j]
            else:
                print("Matrice nisu istih dimenzija.")
        else:  # slucaj da se oduzima sa skalarom
            for i in range(0, self.x):
                for j in range(0, self.y):
                    # print(other)
                    ret[i, j] = self.matrix[i][j] - other

        return ret

    def __mul__(self, other):  # overloadano mnozenje matrica, A*B ili A*3, vraća rezultat množenja
        # print("TU SAM")
        if isinstance(other, Matrica):  # provjera instanci objekta
            ret = Matrica(x=self.x, y=other.y)
            if self.y == other.x:
                for i in range(0, self.x):
                    for k in range(0, other.y):
                        sum = 0
                        for j in range(0, self.y):
                            sum = sum + (self.matrix[i][j] * other.matrix[j][k])

                        ret[i, k] = sum
            else:
                raise "Matrices contain incorrect dimensions"

        else:  # slucaj da je drugi objekt skalar
            ret = Matrica(x=self.x, y=self.y)
            for i in range(0, self.x):
                for j in range(0, self.y):
                    ret[i, j] = self.matrix[i][j] * other

        return ret

    def __rmul__(self, other):  # overloadano mnozenje kada je matrica s desne strane, npr. 3*A
        # print("TU SAM")
        ret = Matrica(x=self.x, y=self.y)
        for i in range(0, self.x):
            for j in range(0, self.y):
                ret[i, j] = self.matrix[i][j] * other

        return ret

    def __str__(
            self):  # format ispisa matrice, vraća string reprezentaciju objekta tipa Matrica, odnosno pripadajuće matrice
        st = ""
        maxstr = 0
        for i in range(0, self.x):
            for j in range(0, self.y):
                curr = len(str(self.matrix[i][j]))
                if curr > maxstr:
                    maxstr = curr

        for i in range(0, self.x):
            for j in range(0, self.y):
                current = str(self.matrix[i][j])
                oduzmi = 0
                if self.matrix[i][j] >= 0:
                    st += " "
                    oduzmi = 1
                st += current + " " * (maxstr + 2 - len(current) - oduzmi)
            st += "\n"
        return st

    def __eq__(self,
               other):  # metoda koja nadjačava operator ==, vraća True ako objekti imaju iste elemente, inače False
        if isinstance(other, Matrica):
            if self.x == other.x and self.y == other.y:
                for i in range(0, self.x):
                    for j in range(0, self.y):
                        if self.matrix[i][j] != other.matrix[i][j]:
                            return False

                return True
            return False
        return False

    def forwardSubstitution(self,
                            vector):  # supstitucija unaprijed, rjesavanje sustava Ly = Pb, gdje je b vektor, a L je donja trokutasta matrica
        rez = Matrica(x=vector.x, y=1)

        for i in range(0, vector.x):
            rez[i, 0] = vector[i, 0]
            for j in range(0, i):
                rez[i, 0] -= self.matrix[i][j] * rez[j, 0]
                if abs(rez[i, 0]) == 0.0:
                    rez[i, 0] = 0.0

        return rez

    def backwardSubstitution(self,
                             vector):  # supstitucija unatrag, rjesavanje sustava Ux = y, nakon dobivenog y-a (ulazni vektor), U je gornja trokutasta matrica
        rez = Matrica(x=vector.x, y=1)

        for i in reversed(range(0, vector.x)):
            rez[i, 0] = vector[i, 0]
            for j in range(i + 1, vector.x):
                rez[i, 0] -= self.matrix[i][j] * rez[j, 0]
            if abs(self.matrix[i][i]) < Matrica.epsilon:  # provjera premalih vrijednosti koja sprijecava gresku
                raise "Cannot divide by zero"
            rez[i, 0] *= (1 / self.matrix[i][i])  # izvodi se ako nije bacen error
            if abs(rez[i, 0]) == 0.0:
                rez[i, 0] = 0.0

        return rez

    # LU i LUP dekompozicija
    def decomposition(self,
                      p):  # implementacija LU i LUP dekompozicija, izbor metode ovisi o argumentu p, vraća permutacijsku matricu, broj promijenjenih redaka te izračunatu gornju i donju trokutastu matricu
        # print(Matrica.epsilon)
        P = Matrica.ones(self.x)
        suma = 0

        for i in range(0, self.x - 1):

            if p:  # ako se izvodi LUP dekompozicija
                max = i

                # za pivot uzmi najvecu vrijednost u stupcu
                for p in range(i + 1, self.x):
                    if abs(self.matrix[p][i]) > abs(self.matrix[max][i]):
                        max = p

                # zamijeni retke ako je pronaden veci stozerni element
                if max != i:
                    suma += 1
                    self.swap(i, max)
                    P.swap(i, max)

                if abs(self.matrix[max][max]) < Matrica.epsilon:
                    raise "Pivot is equal to zero, terminate"

            for j in range(i + 1, self.x):

                if abs(self.matrix[i][
                           i]) < Matrica.epsilon:  # provjera vrijednosti stozernog elementa jer se dijeli s njim
                    raise "Pivot is equal to zero, terminate"

                self.matrix[j][i] /= self.matrix[i][i]

                for k in range(i + 1, self.x):
                    self.matrix[j][k] -= self.matrix[j][i] * self.matrix[i][k]
                    if abs(self.matrix[j][k]) == 0.0:
                        self.matrix[j][k] = 0.0

        return P, suma, Matrica.createL(self), Matrica.createU(self)

    # zamjena redaka na indeksima i i p u matrici
    def swap(self, i, p):
        for k in range(0, self.y):
            save = self.matrix[i][k]
            self.matrix[i][k] = self.matrix[p][k]
            self.matrix[p][k] = save

    # računanje trasnponirane matrice
    def transpose(self):
        ret = Matrica(x=self.y, y=self.x)
        for i in range(0, self.y):
            for j in range(0, self.x):
                ret[i, j] = self.matrix[j][i]

        return ret

    # kreiranje jedinične matrice
    @staticmethod
    def ones(n):
        rez = Matrica(x=n, y=n)
        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    rez[i, j] = 1  # postavi u jedinicu samo elemente dijagonale
                else:
                    rez[i, j] = 0  # ostale elemente stavi u nulu
        return rez

    def determinant(self):  # racunanje determinanti

        if self.x != self.y:
            raise "Matrix has no determinant"
        else:

            P, suma, L, U = self.decomposition(p=True)  # P matrica sa izmijenjenim retcima

            detL = 1
            detU = 1

            for i in range(0, L.x):  # množenje elemenata na dijagonali
                detL *= L[i, i]

            for i in range(0, U.x):
                # print(U[i,i])
                detU *= U[i, i]  # množenje elemenata na dijagonali

            return pow(-1, suma) * detL * detU

    def assign(self, matrica):  # metoda pridruzivanja, npr. A=B
        self.matrix = [[0] * matrica.y for row in range(matrica.x)]
        for i in range(0, matrica.x):
            for j in range(0, matrica.y):
                self.matrix[i][j] = matrica[i, j]

    def printMatrix(self):  # metoda printanja matrice
        print(self)

    @staticmethod
    def createL(matrica):  # stvaranje donje trokutaste matrice, jedinice na dijagonali, elementi samo gdje je j<i
        rez = Matrica(x=matrica.x, y=matrica.y)
        for i in range(0, matrica.x):
            for j in range(0, matrica.y):
                if j < i:
                    rez[i, j] = matrica[i, j]
                elif j == i:
                    rez[i, j] = 1
                else:
                    rez[i, j] = 0

        return rez

    @staticmethod
    def createU(matrica):  # stvaranje gornje trokutaste matrice, elementi samo gdje je j>=i

        rez = Matrica(x=matrica.x, y=matrica.y)
        for i in range(0, matrica.x):
            for j in range(0, matrica.y):
                if j >= i:
                    rez[i, j] = matrica[i, j]
                else:
                    rez[i, j] = 0

        return rez

    @staticmethod
    def calculate(A, v,
                  p):  # funkcija koju se zove za traženje rješenja, argument p javlja o kojoj se dekompoziciji radi, A je matrica s lijeve strane, a v vektor s desne
        if p == 0:
            A.decomposition(p=False)
        else:
            P, suma, L, U = A.decomposition(p=True)
            v = P * v

        y = A.forwardSubstitution(v)
        #print(y)
        x = A.backwardSubstitution(y)
        return x
