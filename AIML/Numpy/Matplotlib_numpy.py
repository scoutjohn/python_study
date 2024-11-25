import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**2 -4*x-5

if __name__ == '__main__':
    print(f(4))
    a = np.arange(-5,5,0.25)
    b = f(a)
    print(b)
    plt.plot(a,b)
    plt.show()
