import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 2*np.pi


def int_rect(f, a, b, N):
    L = b-a
    h = L/N

    X = np.linspace(a+h/2, b-h/2, N)
    Y = f(X)

    return h * Y.sum()

def int_trap(f, a, b, N):
    L = b-a
    h = L/N

    X = np.linspace(a, b, N+1)
    Y = f(X)

    return h/2*(Y[:-1]+Y[1:]).sum()

#wartosc_dokladna = np.exp(b)-np.exp(a)
wartosc_dokladna = b ** 4 / 4 - a ** 4 / 4

hs = []
errs = []
errs_trap = []
for N_float in np.logspace(0, 5, 3*5):
    N = int(round(N_float))
    #blad = int_rect(np.exp, a, b, N) - wartosc_dokladna
    blad = int_rect(lambda X: X ** 3, a, b, N) - wartosc_dokladna
    errs.append(blad)
    #blad_trap = int_trap(np.exp, a, b, N) - wartosc_dokladna
    blad_trap = int_trap(lambda X: X ** 3, a, b, N) - wartosc_dokladna
    errs_trap.append(blad_trap)
    hs.append((b-a)/N)

print('Wyjasnienie: https://math.stackexchange.com/a/674350')

plt.plot(hs, np.abs(errs), label='metoda prostokatow')
plt.plot(hs, np.abs(errs_trap), label='metoda trapezow')
#plt.title('integrate exp(x) dx from 0 to 2pi')
plt.title('integrate x**3 dx from 0 to 2pi')
plt.yscale("log")
plt.ylabel('wartosc bezwzgledna bledu')
plt.xscale("log")
plt.xlabel('krok calkowania')
plt.legend()
plt.show()


