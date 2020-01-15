import matplotlib.pyplot as plt
import sys
import numpy as np

def plot_geron(T):
    X = (T ** 2 - 1) / (T**2 + 1)
    Y = 2 * T * (T**2 - 1)  / (T**2 + 1)**2
    plt.plot(X,Y)
    plt.show()

if __name__ == "__main__":
    t_max = float(sys.argv[1])
    T = np.linspace(-t_max, t_max, 10000)
    plot_geron(T)

