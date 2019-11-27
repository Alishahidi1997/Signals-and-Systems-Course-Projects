import numpy as np
from matplotlib import pyplot as plt

n = np.arange(0, 100)
fig, axe = plt.subplots(1, 1)
L = 50
def heaviside(t):
    return (t >= 0) * 1
def divide_convolve(x,h,l):
    yn = []
    y = []
    for i in range(0,int(100/l)):
        yn.append(np.convolve(x[(l*i):(l*(i+1))],h))
        if(i > 0 ):
            y = np.concatenate([y[0:l],yn[i][0:l]])
        else :
         y = yn[0][0:l]
    return y

def main():
    x = np.cos(n**2) * np.sin(np.pi*n*2/5)
    h = ((9/10)**n)*(heaviside(n)-heaviside(n-10))
    y = divide_convolve(x,h,L)
    axe.stem(n, y)
    axe.set_title("y[n] = y0[n] + y1[n-l]+ ... + yr[n-rl]")
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()