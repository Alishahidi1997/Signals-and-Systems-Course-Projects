import numpy as np
from matplotlib import pyplot as plt

R = 20
n = np.array([n for n in range(-R, R+1)])
fig, axs = plt.subplots(4, 1)


def impulse():
    return np.concatenate([np.zeros(R), np.ones(1), np.zeros(R)])

def sin_xn():
    y1 = np.sin((np.pi/2)*impulse())
    axs[0].stem(n, y1)
    axs[0].set_title('sin impulse')
    y2= np.sin((np.pi) * impulse())
    axs[1].stem(n, y2)
    axs[1].set_title('sin 2impulse')
    y3 = np.sin((np.pi / 2) * (impulse() + 2 * impulse()))
    axs[2].stem(n, y3)
    axs[2].set_title('y2+y1')
    y4 = np.sin((np.pi / 2) * ( 20 * impulse()))
    axs[3].stem(n, y4)
    axs[3].set_title('a*impulse')


def main():
    sin_xn()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
