
import numpy as np
from matplotlib import pyplot as plt
from numpy import fft
from scipy.io import wavfile

phone = []
fig, ax = plt.subplots(2, 1)
row = [0.7217,0.5346, 0.5346, 0.5346,
         0.5906, 0.5906, 0.5906,
         0.6535, 0.6535, 0.6535,
         ]
col = [1.0247, 0.9273, 1.0247, 1.1328,
         0.9273, 1.0247, 1.1328,
         0.9273, 1.0247, 1.1328,
        ]


def show(signal, i ):
    L = len(signal)
    X = fft.fft(signal, n=2048)
    X_abs = 2 * np.abs(X) / L
    half = int(2048 / 2)
    freq = fft.fftfreq(2048, d=1/8192)
    ax[i].plot(freq[:half], X_abs[:half])
    if i == 0 :
        ax[i].set_title('1')
    if i == 1:
        ax[i].set_title('9')
    ax[i].set_xlabel('Frequency [Hz]')
    ax[i].set_ylabel('|X(f)|')
    ax[i].grid()

def main():
    n = np.arange(2048.00)
    for i in range(10):
        phone.append(np.sin(row[i] * n) + np.sin(col[i] * n))
        wavfile.write("./q2/{}_phone.wav".format(i), 8192, phone[i])
    show(phone[1], 0)
    show(phone[9], 1)
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()


