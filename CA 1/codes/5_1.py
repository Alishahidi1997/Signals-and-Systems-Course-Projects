import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0, 30, 0.1)

fig, axs = plt.subplots(4, 1)


def sine():
    x1 =  t + 5 / (np.pi) * np.sin(np.pi * t * 2 / 5)
    axs[0].plot(t, x1)
    axs[0].set_title('x1(t)')
def expn():
    x2 =(12/np.pi) * np.sin(np.pi*t/ 3) + 4*t
    axs[1].plot(t, x2)
    axs[1].set_title('x2(t)')

def impulse():
    # x4 = 32*();
    axs[3].set_title('x4(t)')

def main():
    sine()
    expn()
    impulse()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
