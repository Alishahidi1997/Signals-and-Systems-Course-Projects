
import numpy as np
from scipy.io import wavfile

phone = []

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
        wavfile.write("./q2/ss{}.wav".format(i), 8192, phone[i])
if __name__ == '__main__':
    main()

