import numpy as np
import matplotlib.pyplot as plt

N = 1000
p = 0.25
M = 10000

def eksperyment(N, p):
    sukcesy = 0
    for _ in range(N):
        if np.random.random() < p:
            sukcesy += 1
    return sukcesy



if __name__ == '__main__':
    np.random.seed(42)

    liczba_sukcesow = []
    for _ in range(M):
       liczba_sukcesow.append(eksperyment(N,p))
       # liczba_sukcesow.append(np.random.binomial(N, p))

    plt.hist(liczba_sukcesow,
             bins=np.linspace(200,300,101))
    
    plt.show()
        
    
