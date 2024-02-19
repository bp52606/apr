# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from RungeKutta import RungeKutta
from funkcija import funkcija
from Matrica import Matrica
from Trapez import Trapez
from Euler import Euler
from EulerReverse import EulerReverse
from PrediktorskoKorektorski import PrediktorskoKorektorski


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # x = Ax + B*r(t)

    # 1.

    print("PRVI\n")

    A: Matrica = Matrica(pathToFile="mat1.txt")
    A.createMatrix()

    B: Matrica = Matrica(pathToFile="mat2.txt")
    B.createMatrix()

    x0 = Matrica(pathToFile="x0.txt")

    r: Matrica = Matrica(pathToFile="r1.txt")

    T = 0.01
    tmax = 10

    print("RK:\n")

    func = funkcija(A=A, B=B, r=r)
    rg = RungeKutta(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma, listaMatrica = rg.algorithm(f=func, fname="RungeKnutta1.txt", prvi=True)
    print("SUMA: ", suma)

    print("Trapez:\n")

    trap = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)

    suma, trapez = trap.algorithm(f=func, fname="Trapez1.txt", prvi=True)
    print("SUMA: ", suma)

    print("Euler:\n")

    euler = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma, eulerRez = euler.algorithm(f=func, fname="Euler1.txt", prvi=True)
    print("SUMA: ", suma)

    print("Reverzni Euler:\n")

    eulerTwist = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma, eulerTwistRez = eulerTwist.algorithm(f=func, fname="ReverseEuler1.txt", prvi=True)
    print("SUMA: ", suma)

    print("Prediktorsko-korektorski:\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    predictor = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma, prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, fname="PredCol1.txt", prvi=True)
    print("SUMA: ", suma)

    print("Prediktorsko-korektorski(2):\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma, prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, fname="PredCol1_2.txt", prvi=True)
    print("SUMA: ", suma)

    # 2.
    print("DRUGI\n")

    A: Matrica = Matrica(pathToFile="A2.txt")
    A.createMatrix()

    B: Matrica = Matrica(pathToFile="B2.txt")
    B.createMatrix()

    x0 = Matrica(pathToFile="X2.txt")

    r: Matrica = Matrica(pathToFile="r2.txt")

    T = 0.01
    tmax = 1

    print("RK:\n")

    func = funkcija(A=A, B=B, r=r)
    rg = RungeKutta(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    listaMatrica = rg.algorithm(f=func, fname="RungeKnutta2.txt")

    print("Trapez:\n")

    trap = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)

    trapez = trap.algorithm(f=func, fname="Trapez2.txt")

    print("Euler:\n")

    euler = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerRez = euler.algorithm(f=func, fname="Euler2.txt")

    print("Reverzni Euler:\n")

    eulerTwist = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerTwistRez = eulerTwist.algorithm(f=func, fname="ReverseEuler2.txt")

    print("Prediktorsko-korektorski:\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    predictor = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, fname="PredKor2.txt")

    print("Prediktorsko-korektorski(2):\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, fname="PredKor2_2.txt")

    # 3.

    print("TREĆI\n")

    A: Matrica = Matrica(pathToFile="A3.txt")
    A.createMatrix()

    B: Matrica = Matrica(pathToFile="B3.txt")
    B.createMatrix()

    x0 = Matrica(pathToFile="X3.txt")

    r: Matrica = Matrica(pathToFile="r3.txt")

    T = 0.01
    tmax = 10

    print("RK:\n")

    func = funkcija(A=A, B=B, r=r)
    rg = RungeKutta(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    listaMatrica = rg.algorithm(f=func, fname="RungeKnutta3.txt")

    print("Trapez:\n")

    trap = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)

    trapez = trap.algorithm(f=func, fname="Trapez3.txt")

    print("Euler:\n")

    euler = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerRez = euler.algorithm(f=func, fname="Euler3.txt")

    print("Reverzni Euler:\n")

    eulerTwist = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerTwistRez = eulerTwist.algorithm(f=func, fname="ReverseEuler3.txt")

    print("Prediktorsko-korektorski:\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    predictor = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, fname="PredKor3.txt")

    print("Prediktorsko-korektorski(2):\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, fname="PredKor3_2.txt")

    # 4.

    print("ČETVRTI\n")

    A: Matrica = Matrica(pathToFile="A4.txt")
    A.createMatrix()

    B: Matrica = Matrica(pathToFile="B4.txt")
    B.createMatrix()

    x0 = Matrica(pathToFile="X4.txt")

    T = 0.01
    tmax = 1

    r: Matrica = Matrica(x=2, y=1)
    r[0, 0] = tmax
    r[1, 0] = tmax

    print("RK:\n")

    func = funkcija(A=A, B=B, r=r)
    rg = RungeKutta(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    listaMatrica = rg.algorithm(four=True, f=func, fname="RungeKnutta4.txt")

    print("Trapez:\n")

    trap = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)

    trapez = trap.algorithm(four=True, f=func, fname="Trapez4.txt")

    print("Euler:\n")

    euler = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerRez = euler.algorithm(four=True, f=func, fname="Euler4.txt")

    print("Reverzni Euler:\n")

    eulerTwist = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerTwistRez = eulerTwist.algorithm(four=True, f=func, fname="ReverseEuler4.txt")

    print("Prediktorsko-korektorski:\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    predictor = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, four=True, fname="PredKor4.txt")

    print("Prediktorsko-korektorski(2):\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, four=True, fname="PredKor4_2.txt")