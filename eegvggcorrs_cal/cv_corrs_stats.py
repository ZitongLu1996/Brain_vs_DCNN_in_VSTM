# -*- coding: utf-8

"""
@File       :   sd_corrs_stats.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.stuff import permutation_test

# convs

"""cv_trained = np.loadtxt("corrs_cv/convs/trained/theta_power_fp.txt")
cv_untrained = np.loadtxt("corrs_cv/convs/untrained/theta_power_fp.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/convs/theta_power_fp.txt", p)"""

# fcs

cv_trained = np.loadtxt("corrs_cv/fcs/trained/theta_power_fp.txt")
cv_untrained = np.loadtxt("corrs_cv/fcs/untrained/theta_power_fp.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/fcs/theta_power_fp.txt", p)


# convs

"""cv_trained = np.loadtxt("corrs_cv/convs/trained/theta_power_po.txt")
cv_untrained = np.loadtxt("corrs_cv/convs/untrained/theta_power_po.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/convs/theta_power_po.txt", p)"""

# fcs

cv_trained = np.loadtxt("corrs_cv/fcs/trained/theta_power_po.txt")
cv_untrained = np.loadtxt("corrs_cv/fcs/untrained/theta_power_po.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/fcs/theta_power_po.txt", p)


# convs

"""cv_trained = np.loadtxt("corrs_cv/convs/trained/alpha_power_fp.txt")
cv_untrained = np.loadtxt("corrs_cv/convs/untrained/alpha_power_fp.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/convs/alpha_power_fp.txt", p)"""

# fcs

cv_trained = np.loadtxt("corrs_cv/fcs/trained/alpha_power_fp.txt")
cv_untrained = np.loadtxt("corrs_cv/fcs/untrained/alpha_power_fp.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/fcs/alpha_power_fp.txt", p)


# convs

"""cv_trained = np.loadtxt("corrs_cv/convs/trained/alpha_power_po.txt")
cv_untrained = np.loadtxt("corrs_cv/convs/untrained/alpha_power_po.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/convs/alpha_power_po.txt", p)"""

# fcs

cv_trained = np.loadtxt("corrs_cv/fcs/trained/alpha_power_po.txt")
cv_untrained = np.loadtxt("corrs_cv/fcs/untrained/alpha_power_po.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/fcs/alpha_power_po.txt", p)

# convs

"""cv_trained = np.loadtxt("corrs_cv/convs/trained/erp_fp.txt")
cv_untrained = np.loadtxt("corrs_cv/convs/untrained/erp_fp.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/convs/erp_fp.txt", p)"""

# fcs

cv_trained = np.loadtxt("corrs_cv/fcs/trained/erp_fp.txt")
cv_untrained = np.loadtxt("corrs_cv/fcs/untrained/erp_fp.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/fcs/erp_fp.txt", p)


# convs

"""cv_trained = np.loadtxt("corrs_cv/convs/trained/erp_po.txt")
cv_untrained = np.loadtxt("corrs_cv/convs/untrained/erp_po.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/convs/erp_po.txt", p)"""

# fcs

cv_trained = np.loadtxt("corrs_cv/fcs/trained/erp_po.txt")
cv_untrained = np.loadtxt("corrs_cv/fcs/untrained/erp_po.txt")

p = np.zeros([851], dtype=np.float)
for t in range(851):
    p[t] = permutation_test(cv_trained[:, t], cv_untrained[:, t])

np.savetxt("cv_stats_results/fcs/erp_po.txt", p)