import numpy as np
from matplotlib import pyplot as plt

fig, axs = plt.subplots(1, 1)
A = -10
B = 7
C = -13
D = 16
n = np.array([i for i in range(A+C, B+D+1)])
nx = np.arange(A, B+1)
nh = np.arange(C, D+1)

def impulse(t,t0):
   return (t==t0) *1
def main():
    x =  impulse(nx, A) + impulse(nx, B)
    h = impulse(nh, C) + impulse(nh, D)
    y1 = np.convolve(x,h)
    axs.stem(n, y1)
    axs.set_title('convolve impulse')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
