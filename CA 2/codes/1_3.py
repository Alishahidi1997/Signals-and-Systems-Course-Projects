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
    noise_free = signal.lfilter(b, a, x)
    wavfile.write("./noise_free1.wav", fs, noise_free)
if __name__ == '__main__':
    main()
