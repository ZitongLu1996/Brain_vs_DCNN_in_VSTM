# -*- coding: utf-8

"""
@File       :   plot_cls.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel

cls_trained = np.loadtxt("../corrs_crosscorrs/cls/trained/erp_po.txt")
cls_untrained = np.loadtxt("../corrs_crosscorrs/cls/untrained/erp_po.txt")
print(cls_trained, cls_untrained)

avg_trained = np.average(cls_trained)
avg_untrained = np.average(cls_untrained)
err_trained = np.std(cls_trained, ddof=1)/np.sqrt(6)
err_untrained = np.std(cls_untrained, ddof=1)/np.sqrt(6)

print(ttest_rel(cls_trained, cls_untrained))

fig = plt.gcf()
fig.set_size_inches(8, 10)

plt.bar(1, avg_trained, width=0.5, color="olive", alpha=0.4)
plt.bar(2, avg_untrained, width=0.5, color="yellowgreen", alpha=0.4)
plt.errorbar(1, avg_trained, yerr=err_trained, color="olive",
             fmt='o', elinewidth=6, capsize=10, capthick=6)
plt.errorbar(2, avg_untrained, yerr=err_untrained, color="yellowgreen",
             fmt='o', elinewidth=6, capsize=10, capthick=6)

max = np.max(np.array([avg_trained+err_trained, avg_untrained+err_untrained]))

plt.plot([1, 2], [max+0.04, max+0.04], lw=3, color='black')
plt.text(1.5, max+0.04, '*', fontsize=40)

plt.axhline(y=0, c="black", alpha=0.6, lw=4)

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(4)
ax.spines["bottom"].set_visible(False)

plt.xlim(0.5, 2.5)
plt.ylim(-0.3, 0.5)

plt.tick_params(labelsize=30)
plt.yticks([-0.2, 0, 0.2, 0.4], ["-0.2", "0.0", "0.2", "0.4"])
plt.xticks([1, 2], ["Trained", "Untrained"], fontsize=40)

plt.show()