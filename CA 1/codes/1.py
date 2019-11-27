import  numpy as np
from matplotlib import  pyplot as plt

n = np.array([n for n in range(0, 32)])
n2 = np.array([i for i in range(0, 50)])

fig,axs = plt.subplots(3, 1)

def cos_power_2():
    x1 = np.cos(np.pi * n / 4)**2
    axs[0].stem(x1)
    axs[0].set_title('cos^2(pin/4)')
def sincos():
    x2 = (np.sin(np.pi * n / 4)*np.cos(np.pi * n / 8))
    axs[1].stem(x2)
    axs[1].set_title('sin*cos')
def sin_plus_cos():
    x3 = np.cos(2*np.pi*n2/6) + 3*np.sin(5*np.pi*n2/12)
    axs[2].stem(x3)
    axs[2].set_title('3sin+cos')

def main():
    cos_power_2()
    sincos()
    sin_plus_cos()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
