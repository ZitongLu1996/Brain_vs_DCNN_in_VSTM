# -*- coding: utf-8

"""
@File       :   rdmscorrs_stats.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.stuff import permutation_test

p = np.zeros([851, 851], dtype=np.float)

corrs = np.zeros([6, 851, 851], dtype=np.float)

for sub in range(6):
    corrs[sub] = np.loadtxt("rdmscorrs/erp_po/sub" + str(sub+1) + ".txt")

zcorrs = 0.5*np.log((1+corrs)/(1-corrs))

for i in range(851):
    for j in range(851):
        p[i, j] = permutation_test(zcorrs[:, i, j], np.zeros([6]))
    print(i)

np.savetxt("rdmscorrs/erp_po/p.txt", p)


p = np.zeros([851, 851], dtype=np.float)

corrs = np.zeros([6, 851, 851], dtype=np.float)

for sub in range(6):
    corrs[sub] = np.loadtxt("rdmscorrs/erp_fp/sub" + str(sub+1) + ".txt")

zcorrs = 0.5*np.log((1+corrs)/(1-corrs))

for i in range(851):
    for j in range(851):
        p[i, j] = permutation_test(zcorrs[:, i, j], np.zeros([6]))
    print(i)

np.savetxt("rdmscorrs/erp_fp/p.txt", p)


p = np.zeros([851, 851], dtype=np.float)

corrs = np.zeros([6, 851, 851], dtype=np.float)

for sub in range(6):
    corrs[sub] = np.loadtxt("rdmscorrs/theta_power_po/sub" + str(sub+1) + ".txt")

zcorrs = 0.5*np.log((1+corrs)/(1-corrs))

for i in range(851):
    for j in range(851):
        p[i, j] = permutation_test(zcorrs[:, i, j], np.zeros([6]))
    print(i)

np.savetxt("rdmscorrs/theta_power_po/p.txt", p)


p = np.zeros([851, 851], dtype=np.float)

corrs = np.zeros([6, 851, 851], dtype=np.float)

for sub in range(6):
    corrs[sub] = np.loadtxt("rdmscorrs/theta_power_fp/sub" + str(sub+1) + ".txt")

zcorrs = 0.5*np.log((1+corrs)/(1-corrs))

for i in range(851):
    for j in range(851):
        p[i, j] = permutation_test(zcorrs[:, i, j], np.zeros([6]))
    print(i)

np.savetxt("rdmscorrs/theta_power_fp/p.txt", p)


p = np.zeros([851, 851], dtype=np.float)

corrs = np.zeros([6, 851, 851], dtype=np.float)

for sub in range(6):
    corrs[sub] = np.loadtxt("rdmscorrs/alpha_power_po/sub" + str(sub+1) + ".txt")

zcorrs = 0.5*np.log((1+corrs)/(1-corrs))

for i in range(851):
    for j in range(851):
        p[i, j] = permutation_test(zcorrs[:, i, j], np.zeros([6]))
    print(i)

np.savetxt("rdmscorrs/alpha_power_po/p.txt", p)


p = np.zeros([851, 851], dtype=np.float)

corrs = np.zeros([6, 851, 851], dtype=np.float)

for sub in range(6):
    corrs[sub] = np.loadtxt("rdmscorrs/alpha_power_fp/sub" + str(sub+1) + ".txt")

zcorrs = 0.5*np.log((1+corrs)/(1-corrs))

for i in range(851):
    for j in range(851):
        p[i, j] = permutation_test(zcorrs[:, i, j], np.zeros([6]))
    print(i)

np.savetxt("rdmscorrs/alpha_power_fp/p.txt", p)