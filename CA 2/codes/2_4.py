import numpy as np
from matplotlib import pyplot as plt
from numpy import fft
from scipy.io import wavfile
row = [0.7217,0.5346, 0.5346, 0.5346,
         0.5906, 0.5906, 0.5906,
         0.6535, 0.6535, 0.6535,
         ]
col = [1.0247, 0.9273, 1.0247, 1.1328,
         0.9273, 1.0247, 1.1328,
         0.9273, 1.0247, 1.1328,
        ]

phone = []
fig, ax = plt.subplots(2, 1)
space = np.zeros(100)
phone_read = []
num_phone1 = []
num_phone2 = []

def plot_num(inp):
    fig, ax = plt.subplots(len(inp), 1)
    for i, j in enumerate(inp):
        L = len(j)
        X = fft.fft(j, n=2048)
        X_abs = 2 * np.abs(X) / L
        freq = fft.fftfreq(2048, d=1 / 8192)
        ax[i].plot(freq[:1024], X_abs[:1024])
        ax[i].set_title(i + 1)
        ax[i].set_xlabel('Frequency [Hz]')
        ax[i].set_ylabel('|X(f)|')
        ax[i].grid()

def main():
    n = np.arange(1000.0)
    for i in range(10):
        phone.append(np.sin(row[i] * n) + np.sin(col[i] * n))
        wavfile.write("./q2/{}_phone.wav".format(i), 8192, phone[i])
    phone_read.append(list(map(float, open("phone1.csv").readline().split(','))))
    phone_read.append(list(map(float, open("phone2.csv").readline().split(','))))
    for i in range(2):
        while len(phone_read[i]) > 1000:
            if i == 0:
                num_phone1.append(phone_read[i][:1000])
            else:
                num_phone2.append(phone_read[i][:1000])
            phone_read[i] = phone_read[i][1100:]
    plot_num(num_phone1)
    plot_num(num_phone2)
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()


