# -*- coding: utf-8

"""
@File       :   fft_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy import signal

N = 500
f = 250

fft_rlts = np.zeros([6, 11, N], dtype=np.float)

for sub in range(1):

    sub = sub +4

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/untrained/alpha_power_fp/sub" + str(sub+1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    for ly in range(1):

        corrs_ly = corrs[ly, 113+250+125:113+250+375, 0]
        avg = np.average(corrs_ly)
        corrs_ly = corrs_ly - avg
        y = np.zeros([N])
        y[:250] = corrs_ly
        fft_y = fft(y)
        x = np.arange(N)
        abs_y = np.abs(fft_y)

        #b, a = signal.butter(2, 2*200/10000, 'lowpass')
        #abs_y = signal.filtfilt(b, a, abs_y)

        plt.plot(f*x[:100]/N, abs_y[:100])
        plt.show()

        #fft_rlts[sub, ly] = abs_y

#fft_rlts = np.reshape(fft_rlts, [6*11, N])
#np.savetxt("fft_rlts/trained/erp_fp.txt", fft_rlts)