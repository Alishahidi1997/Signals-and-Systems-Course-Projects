import numpy as np
from scipy.io import wavfile
from scipy import signal
from numpy import fft
from matplotlib import pyplot as plt

fs, x = wavfile.read("./soundCA2.wav")
def nextpow2(x):
    return (x - 1).bit_length()
def find_noise(x,f):
    print(f[np.where(max(x) == x)])

def main():
    L = len(x)
    print('L =', L)
    NFFT = 2 ** nextpow2(L)  # Next power of 2 from length of x
    X = fft.fft(x, n=NFFT)
    X_abs = 2 * np.absolute(X) / L
    half = int(NFFT/2)
    freq = fft.fftfreq(NFFT, d=1/fs)
    find_noise(X_abs[:half], freq[:half])
    fig, ax = plt.subplots(1, 1)
    ax.plot(freq[:half], X_abs[:half])
    ax.set_title('Single-Sided Amplitude Spectrum of x(t)')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('|X(f)|')
    ax.grid()
    plt.show()

if __name__ == '__main__':
    main()
