import numpy as np
from matplotlib import pyplot as plt

xn1 = np.array([i for i in range(0, 8)])
xn2 = np.array([i for i in range(0, 16)])
xn3 = np.array([i for i in range(0, 32)])
fig, axe = plt.subplots(3, 1)

def func(t):
    return (t <= 7) * 1

def period(n, p):
    return np.concatenate([n for i in range(p)])

def main():
    x1 = period(func(xn1),8)
    axe[0].stem(x1)
    axe[0].set_title('x1[n]')
    x2 = period(func(xn2),4)
    axe[1].stem(x2)
    axe[1].set_title('x2[n]')
    x3 = period(func(xn3),2)
    axe[2].stem(x3)
    axe[2].set_title('x3[n]')
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()