import matplotlib.pyplot as plt
import numpy as np

def plot_pi(n):
    ax = plt.gca()
    ax.set_aspect('equal')
    T=np.linspace(0, 2*np.pi, 100)
    ax.plot(np.sin(T), np.cos(T), color='k')
    ax.plot([-1,-1,1,1,-1], [1,-1, -1,1, 1], color='k')
    points = np.random.uniform(-1, 1, size=(2, n))
    X, Y = points
    ax.plot(X, Y, linestyle='none', marker='.')
    #m=0
    #for x,y in points.T:
    #    if x**2+y**2<1:
    #        m+=1
    m = ((points**2).sum(axis=0) < 1).sum()
    ax.set_title(str(4*m/n))

def calculate_pi(n):
   
    points = np.random.uniform(-1, 1, size=(2, n))
    #m=0
    #for x,y in points.T:
    #    if x**2+y**2<1:
    #        m+=1
    m = ((points**2).sum(axis=0) < 1).sum()
    return 4*m/n

if __name__ == '__main__':
    np.random.seed(42)
    plot_pi(100)
    plt.figure()
    ax= plt.subplot(2,1,1)
    ns = []
    pis = []
    k = 10
    for n in [10, 100, 1000, 10000]:
        for _ in range (k):
            pi = calculate_pi(n)
            ns.append(n)
            pis.append(pi)
    ax.scatter(ns, pis)
    ax.set_xscale('log')
    plt.show()
    


