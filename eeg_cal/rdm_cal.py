# -*- coding: utf-8

"""
@File       :   rdm_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.rdm_cal import eegRDM

for sub in range(6):

    data = np.loadtxt("../eegdata/alpha_power_po/sub" + str(sub+1) + ".txt")
    data = np.reshape(data, [18, 1, 1, 17, 875])

    eegrdms = eegRDM(data, time_opt=1, time_win=25, time_step=1)
    eegrdms = np.reshape(eegrdms, [851, 18*18])

    np.savetxt("../eegrdm/alpha_power_po/sub" + str(sub+1) + ".txt", eegrdms)