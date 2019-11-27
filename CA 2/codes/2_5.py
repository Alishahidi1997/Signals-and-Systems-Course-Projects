import numpy as np
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
space = np.zeros(100)
phone_read = []
num_phone1 = []
num_phone2 = []

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
    numphone = []
    numphone.append(num_phone1)
    numphone.append(num_phone2)
    for p in numphone:
        print("Phone :")
        for num in p:
            for i, j in enumerate(phone):
                if np.allclose(num, j, atol=1):
                    print(i)

if __name__ == '__main__':
    main()


