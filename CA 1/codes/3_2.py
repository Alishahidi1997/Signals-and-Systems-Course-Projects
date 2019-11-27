import numpy as np
from matplotlib import pyplot as plt

fig, axs = plt.subplots(3, 1)
n = np.array([n for n in range(-6, 10)])

def stepn():
    step_n =  np.concatenate([np.zeros(6), np.ones(10)])
    axs[0].stem(n, step_n)
def stepn1():
    step_n1 = np.concatenate([np.zeros(5), np.ones(11)])
    axs[1].stem(n, step_n1)
def output():
    return np.concatenate([np.zeros(5), np.ones(11)]) +  np.concatenate([np.zeros(6), np.ones(10)])

def main():
    stepn()
    axs[0].set_title('x[n]')
    stepn1()
    axs[1].set_title('x[n+1]')
    axs[2].stem(n, output())
    axs[2].set_title('x[n]+x[n+1]')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
