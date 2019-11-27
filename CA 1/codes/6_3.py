import numpy as np
from matplotlib import pyplot as plt

a = 0
b = 24
c = 0
d = 14

fig, axe = plt.subplots(1,1)
n = np.array([i for i in range(a+c, b+d+1)])
nx = np.array([i for i in range(a, b+1)])
nh = np.array([i for i in range(c, d+1)])

def heaviside(t):
    return (t >= 0) *1

def main():
    x = (0.5 **(nx-2))*heaviside(nx-2)
    h = heaviside(nh+2)
    y = np.convolve(x, h)
    axe.stem(n,y)
    axe.set_title('y[n]= x[n]*h[n]')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()