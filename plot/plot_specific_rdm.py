# -*- coding: utf-8

"""
@File       :   specific_rdm.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.rsa_plot import plot_rdm

eegrdms_po = np.zeros([6, 851, 18, 18], dtype=np.float)

for sub in range(6):
    subeegrdms = np.loadtxt("../eegrdm/alpha_power_po/sub" + str(sub+1) + ".txt")
    print(subeegrdms.shape)
    subeegrdms = np.reshape(subeegrdms, [851, 18, 18])
    eegrdms_po[sub] = subeegrdms

avgeegrdms_po = np.average(eegrdms_po, axis=0)

eegrdms_fp = np.zeros([6, 851, 18, 18], dtype=np.float)

for sub in range(6):
    subeegrdms = np.loadtxt("../eegrdm/alpha_power_fp/sub" + str(sub+1) + ".txt")
    print(subeegrdms.shape)
    subeegrdms = np.reshape(subeegrdms, [851, 18, 18])
    eegrdms_fp[sub] = subeegrdms

avgeegrdms_fp = np.average(eegrdms_fp, axis=0)

conditions = ["left 10°", "left 30°", "left 50°", "left 70°", "left 90°", "left 110°", "left 130°", "left 150°", "left 170°",
              "right 10°", "right 30°", "right 50°", "right 70°", "right 90°", "right 110°", "right 130°", "right 150°", "right 170°"]
t = 0.45
m = int(t/0.004)+125
plot_rdm(avgeegrdms_po[m], conditions=conditions)
plot_rdm(avgeegrdms_fp[m], conditions=conditions)
t = 1.4
m = int(t/0.004)+125
plot_rdm(avgeegrdms_po[m], conditions=conditions)
plot_rdm(avgeegrdms_fp[m], conditions=conditions)
t = 2.0
m = int(t/0.004)+125
plot_rdm(avgeegrdms_po[m], conditions=conditions)
plot_rdm(avgeegrdms_fp[m], conditions=conditions)