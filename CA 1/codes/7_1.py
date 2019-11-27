import numpy as np
from matplotlib import pyplot as plt

n = np.arange(0, 100)
fig, axe = plt.subplots(1, 1)

def heaviside(t):
    return (t >= 0) * 1

def main():
    x = np.cos(n**2) * np.sin(np.pi*n*2/5)
    h = ((9/10)**n)*(heaviside(n)-heaviside(n-10))
    y = np.convolve(x, h)
    axe.stem(n, y[0:100])
    axe.set_title("y[n] = x[n] * h[n]")
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()