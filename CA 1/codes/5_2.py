import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0.1, 60, 0.1)
fig, axs = plt.subplots(4, 1)


def sinp():
    x1 = t + 5 / (np.pi) * np.sin(np.pi * t * 2 / 5)
    axs[0].plot(t, x1/(2*t))
    axs[0].set_title('x1(t)')


def expp():
    x2 = (12 / np.pi) * np.sin(np.pi * t / 3) + 4 * t
    axs[1].plot(t, x2/(2*t))
    axs[1].set_title('x2(t)')


def impulsep():
   axs[3].set_title('x4(t)')


def main():
    sinp()
    expp()
    impulsep()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
