# -*- coding: utf-8

"""
@File       :   rdmscorrs_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from scipy.stats import spearmanr

def rdm_correlation_spearman(RDM1, RDM2, rescale=False):

    # get number of conditions
    cons = np.shape(RDM1)[0]

    # calculate the number of value above the diagonal in RDM
    n = int(cons*(cons-1)/2)

    if rescale == True:

        # flatten the RDM1
        vrdm = np.reshape(RDM1, [cons*cons])
        # array -> set -> list
        svrdm = set(vrdm)
        lvrdm = list(svrdm)
        lvrdm.sort()

        # get max & min
        maxvalue = lvrdm[-1]
        minvalue = lvrdm[1]

        # rescale
        if maxvalue != minvalue:

            for i in range(cons):
                for j in range(cons):

                    # not on the diagnal
                    if i != j:
                        RDM1[i, j] = float((RDM1[i, j] - minvalue) / (maxvalue - minvalue))

        # flatten the RDM2
        vrdm = np.reshape(RDM2, [cons * cons])
        # array -> set -> list
        svrdm = set(vrdm)
        lvrdm = list(svrdm)
        lvrdm.sort()

        # get max & min
        maxvalue = lvrdm[-1]
        minvalue = lvrdm[1]

        # rescale
        if maxvalue != minvalue:

            for i in range(cons):
                for j in range(cons):

                    # not on the diagnal
                    if i != j:
                        RDM2[i, j] = float((RDM2[i, j] - minvalue) / (maxvalue - minvalue))

    # initialize two vectors to store the values above the diagnal of two RDMs
    v1 = np.zeros([n], dtype=np.float64)
    v2 = np.zeros([n], dtype=np.float64)

    # assignment
    nn = 0
    for i in range(cons-1):
        for j in range(cons-1-i):
            v1[nn] = RDM1[i, i+j+1]
            v2[nn] = RDM2[i, i+j+1]
            nn = nn + 1

    # calculate the Spearman Correlation
    rp = np.array(spearmanr(v1, v2))

    return rp

for sub in range(6):

    subrdms = np.loadtxt("../eegrdm/erp_fp/sub" + str(sub + 1) + ".txt")
    subrdms = np.reshape(subrdms, [851, 18, 18])

    subcorrs = np.zeros([851, 851], dtype=np.float)

    for i in range(851):
        for j in range(851):
            subcorrs[i, j] = rdm_correlation_spearman(subrdms[i], subrdms[j])[0]
            print(i, j)

    np.savetxt("rdmscorrs/erp_fp/sub" + str(sub+1) + ".txt", subcorrs)