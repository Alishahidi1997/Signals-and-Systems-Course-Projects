import numpy as np
from matplotlib import pyplot as plt
xn1=[]
xn1.append( np.array([i for i in range(0, 8)]))
xn1.append(np.array([i for i in range(0, 16)]))
xn1.append(np.array([i for i in range(0, 32)]))
fig, axe = plt.subplots(3, 3)

def func(t):
    return (t <= 7) * 1

def period(n, p):
    return np.concatenate([n for i in range(p)])
def x(p,z):
    a = np.fft.fft(func(xn1[z]))/p
    axe[z,0].stem(np.real(a))
    axe[z,0].set_title('real')
    axe[z, 1].stem(np.imag(a))
    axe[z, 1].set_title('img')
    axe[z, 2].stem(abs(a))
    axe[z, 2].set_title('abs(a)')

def main():
    x(8,0)
    x(32,1)
    x(16,2)
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()

