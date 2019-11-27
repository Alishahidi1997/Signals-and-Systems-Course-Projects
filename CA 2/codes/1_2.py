import numpy as np
from scipy.io import wavfile
from scipy import signal
from numpy import fft
from matplotlib import pyplot as plt

fs, x = wavfile.read("./soundCA2.wav")
def nextpow2(x):
    return (x - 1).bit_length()
def butter_bandstop_filter(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = signal.butter(N=order, Wn=[low, high], btype='bandstop')
        return b, a
def main():
    b, a = butter_bandstop_filter(1540, 1660, fs)
    f,y = signal.freqz(b, a)
    noise_free = signal.lfilter(b, a, x)
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(f, y)
    ax[0].set_title('Filter')
    ax[0].set_xlabel('omega')
    ax[0].set_ylabel('impulse freq response')
    ax[0].grid()
    L = len(noise_free)
    print('L =', L)
    NFFT = 2 ** nextpow2(L)  # Next power of 2 from length of x
    X = fft.fft(noise_free, n=NFFT)
    X_abs = 2 * np.absolute(X) / L
    half = int(NFFT/2)
    freq = fft.fftfreq(NFFT, d=1/fs)
    ax[1].plot(freq[:half], X_abs[:half])
    ax[1].set_title('Single-Sided Amplitude Spectrum of x(t)')
    ax[1].set_xlabel('Frequency [Hz]')
    ax[1].set_ylabel('|X(f)|')
    ax[1].grid()
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()
