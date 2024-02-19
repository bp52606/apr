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
    listaMatrica = rg.algorithm(f=func,fname="RungeKnutta2.txt")

    print("Trapez:\n")

    trap = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)

    trapez = trap.algorithm(f=func,fname="Trapez2.txt")

    print("Euler:\n")

    euler = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerRez = euler.algorithm(f=func,fname="Euler2.txt")

    print("Reverzni Euler:\n")

    eulerTwist = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    eulerTwistRez = eulerTwist.algorithm(f=func,fname="ReverseEuler2.txt")

    print("Prediktorsko-korektorski:\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    predictor = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10, predictor=predictor, kontroler=kontroler,fname="PredKor2.txt")

    print("Prediktorsko-korektorski(2):\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    prekor.pred_kor(f=func, iter=10,predictor=predictor, kontroler=kontroler,fname="PredKor2_2.txt")

