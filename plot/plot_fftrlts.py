# -*- coding: utf-8

"""
@File       :   plot_fftrlts.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt

ffts = np.loadtxt("../corrs_fft/fft_rlts/trained/erp_po.txt")
ffts = np.reshape(ffts, [6, 11, 1000])

powers = ffts[:, 1, :100]

avg = np.average(powers, axis=0)
err = np.zeros([100], dtype=np.float)
for t in range(100):
    err[t] = np.std(powers[:, t], ddof=1)/np.sqrt(6)

x = np.arange(0, 25, 0.25)

plt.fill_between(x, avg-err, avg+err, label='Trained', alpha=0.9)

plt.xlim(0, 25)
plt.ylim(0, )
plt.show()