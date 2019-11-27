from matplotlib import pyplot as plt
import numpy as np

fig, axs = plt.subplots(5, 1)
t = np.arange(-2, 5.5, 0.1)

def heaviside(t):
    return (t >= 0) * 1

def f(t):
    return t * (heaviside(t) - heaviside(t - 2))

def plote():
    axs[0].plot(t, f(-t))
    axs[0].set_title('g1(t)')
    axs[1].plot(t, f(t+1))
    axs[1].set_title('g2(t)')
    axs[2].plot(t, f(t-3))
    axs[2].set_title('g3(t)')
    axs[3].plot(t, f(-t+1))
    axs[3].set_title('g4(t)')
    axs[4].plot(t, f(-2*t+1))
    axs[4].set_title('g5(t)')
def main():
    plote()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()