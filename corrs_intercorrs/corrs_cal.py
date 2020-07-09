# -*- coding: utf-8

"""
@File       :   corrs_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import math
from scipy.stats import spearmanr

# for conv layers

ils_trained = np.zeros([6], dtype=np.float)
ils_untrained = np.zeros([6], dtype=np.float)

for sub in range(6):

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/trained/erp_fp/sub" + str(sub+1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[:8, 113:, 0]

    n = int(math.factorial(8)/(2*math.factorial(8-2)))

    rcorrs = np.zeros([n], dtype=np.float)

    index = 0

    for i in range(8):
        for j in range(8):
            if i != j and i < j:
                rcorrs[index] = spearmanr(rs[i], rs[j])[0]
                index = index + 1

    print(np.average(rcorrs))

    ils_trained[sub] = np.average(rcorrs)

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/untrained/erp_fp/sub" + str(sub + 1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[:8, 113:, 0]

    n = int(math.factorial(8) / (2 * math.factorial(8 - 2)))

    rcorrs = np.zeros([n], dtype=np.float)

    index = 0

    for i in range(8):
        for j in range(8):
            if i != j and i < j:
                rcorrs[index] = spearmanr(rs[i], rs[j])[0]
                index = index + 1

    print(np.average(rcorrs))

    ils_untrained[sub] = np.average(rcorrs)

    print("***")

np.savetxt("ils/convs/trained/erp_fp.txt", ils_trained)
np.savetxt("ils/convs/untrained/erp_fp.txt", ils_untrained)

# for fc layers

ils_trained = np.zeros([6], dtype=np.float)
ils_untrained = np.zeros([6], dtype=np.float)

for sub in range(6):

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/trained/erp_fp/sub" + str(sub+1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[8:, 113:, 0]

    n = int(math.factorial(3)/(2*math.factorial(3-2)))

    rcorrs = np.zeros([n], dtype=np.float)

    index = 0

    for i in range(3):
        for j in range(3):
            if i != j and i < j:
                rcorrs[index] = spearmanr(rs[i], rs[j])[0]
                index = index + 1

    print(np.average(rcorrs))

    ils_trained[sub] = np.average(rcorrs)

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/untrained/erp_fp/sub" + str(sub + 1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[8:, 113:, 0]

    n = int(math.factorial(3) / (2 * math.factorial(3 - 2)))

    rcorrs = np.zeros([n], dtype=np.float)

    index = 0

    for i in range(3):
        for j in range(3):
            if i != j and i < j:
                rcorrs[index] = spearmanr(rs[i], rs[j])[0]
                index = index + 1

    print(np.average(rcorrs))

    ils_untrained[sub] = np.average(rcorrs)

    print("***")

np.savetxt("ils/fcs/trained/erp_fp.txt", ils_trained)
np.savetxt("ils/fcs/untrained/erp_fp.txt", ils_untrained)
