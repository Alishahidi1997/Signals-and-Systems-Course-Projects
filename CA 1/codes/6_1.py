import numpy as np
from matplotlib import pyplot as plt
R = 10
fig, axs = plt.subplots(1, 1)
n = np.array([n for n in range(-R, R+1)])
nconvolve = np.array([n for n in range(-(2*R), (2*R+1))])

def impulse(t, t0):
    return (t==t0)* 1


def main():
    x =  impulse(n,0) + impulse(n,-2)
    h = 2*impulse(n,1) - 2*impulse(n,-1)
    y1 = np.convolve(x,h)
    axs.stem(nconvolve, y1)
    axs.set_title('convolve impulse')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()



