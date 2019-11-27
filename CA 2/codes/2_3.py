
import numpy as np
from matplotlib import pyplot as plt
from numpy import fft
from scipy.io import wavfile

phone = []
fig, ax = plt.subplots(2, 1)
space = np.zeros(100)

row = [0.7217,0.5346, 0.5346, 0.5346,
         0.5906, 0.5906, 0.5906,
         0.6535, 0.6535, 0.6535,
         ]
col = [1.0247, 0.9273, 1.0247, 1.1328,
         0.9273, 1.0247, 1.1328,
         0.9273, 1.0247, 1.1328,
        ]

def main():
    n = np.arange(2048.00)
    for i in range(10):
        phone.append(np.sin(row[i] * n) + np.sin(col[i] * n))
        wavfile.write("./q2/{}_phone.wav".format(i), 8192, phone[i])
    student_num = [phone[0], space, phone[1], space, phone[9], space, phone[4], space, phone[3], space, phone[4], space, phone[1], space]
    sig = np.concatenate(student_num)
    wavfile.write("./q2/sid.wav", 8192, sig)
if __name__ == '__main__':
    main()


