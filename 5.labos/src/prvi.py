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
    suma, listaMatrica = rg.algorithm(f=func,fname="RungeKnutta1.txt", prvi = True)
    print("SUMA: ",suma)

    print("Trapez:\n")

    trap = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)

    suma,trapez = trap.algorithm(f=func,fname="Trapez1.txt", prvi = True)
    print("SUMA: ", suma)

    print("Euler:\n")

    euler = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma,eulerRez = euler.algorithm(f=func,fname="Euler1.txt",prvi = True)
    print("SUMA: ",suma)

    print("Reverzni Euler:\n")

    eulerTwist = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma,eulerTwistRez = eulerTwist.algorithm(f=func,fname="ReverseEuler1.txt", prvi = True)
    print("SUMA: ",suma)

    print("Prediktorsko-korektorski:\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    predictor = Euler(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = Trapez(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma,prekor.pred_kor(f=func, iter=10,predictor=predictor, kontroler=kontroler,fname="PredCol1.txt", prvi = True)
    print("SUMA: ",suma)

    print("Prediktorsko-korektorski(2):\n")

    prekor = PrediktorskoKorektorski(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    kontroler = EulerReverse(x=x0, t=tmax, T=T, A=A, B=B, r=r)
    suma,prekor.pred_kor(f=func, iter=10,predictor=predictor, kontroler=kontroler,fname="PredCol1_2.txt", prvi = True)
    print("SUMA: ",suma)