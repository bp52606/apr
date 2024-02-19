from RungeKutta import RungeKutta
from funkcija import funkcija
from Matrica import Matrica
from Trapez import Trapez
from Euler import Euler
from EulerReverse import EulerReverse
from PrediktorskoKorektorski import PrediktorskoKorektorski



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # x = Ax + B*r(t)

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
    listaMatrica = rg.algorithm(four=True,f=func,fname="RungeKnutta4.txt")

    print("Trapez:\n")

    trap = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)

    trapez = trap.algorithm(four=True,f=func,fname="Trapez4.txt")

    print("Euler:\n")

    euler = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerRez = euler.algorithm(four=True,f=func,fname="Euler4.txt")

    print("Reverzni Euler:\n")

    eulerTwist = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerTwistRez = eulerTwist.algorithm(four=True, f=func,fname="ReverseEuler4.txt")

    print("Prediktorsko-korektorski:\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    predictor = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler, four=True, fname="PredKor4.txt")

    print("Prediktorsko-korektorski(2):\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10,predictor=predictor, kontroler=kontroler, four=True, fname="PredKor4_2.txt")