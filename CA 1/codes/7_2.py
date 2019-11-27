import numpy as np
from matplotlib import pyplot as plt

n = np.arange(0, 100)
fig, axe = plt.subplots(1, 1)

def heaviside(t):
    return (t >= 0) * 1

def main():
    x = np.cos(n**2) * np.sin(np.pi*n*2/5)
    h = ((9/10)**n)*(heaviside(n)-heaviside(n-10))
    y1 = np.convolve(x[0:50], h)
    y2 = np.convolve(x[50:100], h)

    y =  np.concatenate([y1[0:50], y2[0:50]])
    axe.stem(n, y)
    axe.set_title("y[n] = y0[n] + y1[n-50]")
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()