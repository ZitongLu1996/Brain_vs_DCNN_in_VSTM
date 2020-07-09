# -*- coding: utf-8

"""
@File       :   plot_ils.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel

# for convs layers

ils_trained = np.loadtxt("../corrs_intercorrs/ils/convs/trained/erp_po.txt")
ils_untrained = np.loadtxt("../corrs_intercorrs/ils/convs/untrained/erp_po.txt")
print(ils_trained, ils_untrained)

avg_trained = np.average(ils_trained)
avg_untrained = np.average(ils_untrained)
err_trained = np.std(ils_trained, ddof=1)/np.sqrt(6)
err_untrained = np.std(ils_untrained, ddof=1)/np.sqrt(6)

print(ttest_rel(ils_trained, ils_untrained))

fig = plt.gcf()
fig.set_size_inches(8, 10)

plt.bar(1, avg_trained, width=0.5, color="olive", alpha=0.4)
plt.bar(2, avg_untrained, width=0.5, color="yellowgreen", alpha=0.4)
plt.errorbar(1, avg_trained, yerr=err_trained, color="olive",
             fmt='o', elinewidth=6, capsize=10, capthick=6)
plt.errorbar(2, avg_untrained, yerr=err_untrained, color="yellowgreen",
             fmt='o', elinewidth=6, capsize=10, capthick=6)

plt.plot([1, 2], [avg_trained+err_trained+0.02, avg_trained+err_trained+0.02], lw=3, color='black')
plt.text(1.5, avg_trained+err_trained+0.02, '*', fontsize=40)

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(4)
ax.spines["bottom"].set_linewidth(4)

plt.xlim(0.5, 2.5)
plt.ylim(0, 1)

plt.tick_params(labelsize=30)
plt.xticks([1, 2], ["Trained", "Untrained"], fontsize=40)

plt.show()


# for fc layers

"""ils_trained = np.loadtxt("../corrs_intercorrs/ils/fcs/trained/erp_fp.txt")
ils_untrained = np.loadtxt("../corrs_intercorrs/ils/fcs/untrained/erp_fp.txt")
print(ils_trained, ils_untrained)

avg_trained = np.average(ils_trained)
avg_untrained = np.average(ils_untrained)
err_trained = np.std(ils_trained, ddof=1)/np.sqrt(6)
err_untrained = np.std(ils_untrained, ddof=1)/np.sqrt(6)

print(ttest_rel(ils_trained, ils_untrained))

fig = plt.gcf()
fig.set_size_inches(8, 10)

plt.bar(1, avg_trained, width=0.5, color="olive", alpha=0.4)
plt.bar(2, avg_untrained, width=0.5, color="yellowgreen", alpha=0.4)
plt.errorbar(1, avg_trained, yerr=err_trained, color="olive",
             fmt='o', elinewidth=6, capsize=10, capthick=6)
plt.errorbar(2, avg_untrained, yerr=err_untrained, color="yellowgreen",
             fmt='o', elinewidth=6, capsize=10, capthick=6)

plt.plot([1, 2], [avg_trained+err_trained+0.04, avg_trained+err_trained+0.04], lw=3, color='black')
plt.text(1.5, avg_trained+err_trained+0.04, '*', fontsize=40)

plt.axhline(y=0, c="black", alpha=0.6, lw=4)

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(4)
ax.spines["bottom"].set_visible(False)

plt.xlim(0.5, 2.5)
plt.ylim(-0.2, 0.8)

plt.tick_params(labelsize=30)
plt.xticks([1, 2], ["Trained", "Untrained"], fontsize=40)

plt.show()"""