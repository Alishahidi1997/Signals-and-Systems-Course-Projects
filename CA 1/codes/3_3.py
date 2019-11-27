import numpy as np
from matplotlib import pyplot as plt

fig, axs = plt.subplots(1, 1)
f = np.linspace(0.00001, 2 , 30)

def main():
    x1 = np.log(f)
    axs.stem(f, x1)
    axs.set_title('log(x[n])')
    plt.tight_layout()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
