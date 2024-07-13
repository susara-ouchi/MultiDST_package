from multidst.methods.bonf import bonferroni
from multidst.methods.holm_bonf import holm
from multidst.methods.sgof import sgof_test
from multidst.methods.BH import bh_method
from multidst.methods.qval import q_value
from multidst.methods.BY import BY_method

import pandas as pd

# from multidst.utils.visualization import draw_histogram
from multidst.utils.visualization import sigindex_plot
# from multidst.utils.visualization import draw_p_bar_chart
# from multidst.utils.visualization import fire_hist


def multitest(p_values, alpha=0.05, sigplot=False, results = False):
    """
    Conducts all 06 multiple testing methods to return significant indices under each method.
    Input: list of p-values, threshold, weights (list)
    Return:Dict of sig indices and q-value estimate by Storey's method
    """
    # 0 - Uncorrected
    sig_index = [index for index, p in enumerate(p_values) if p < alpha]
    # uncorrected_count = len(sig_index)

    # 1 - Bonferroni
    bonf_results = bonferroni(p_values, alpha=alpha)
    bonf_p, sig_bonf_p = bonf_results[0], bonf_results[1]
    # bonf_count = len(sig_bonf_p)

    # 2 - Holm
    holm_results = holm(p_values, alpha=alpha)
    holm_p, sig_holm_p = holm_results[0], holm_results[1]
    # holm_count = len(sig_holm_p)

    # 3 - SGoF
    sgof_results = sgof_test(p_values, alpha=alpha)
    sgof_p, sig_sgof_p = sgof_results[0], sgof_results[1]
    # sgof_count = len(sig_sgof_p)

    # 4 - BH
    bh_results = bh_method(p_values, alpha=alpha)
    bh_p, sig_bh_p = bh_results[0], bh_results[1]
    # bh_count = len(sig_bh_p)

    # 5 - BY
    by_results = BY_method(p_values, alpha=alpha)
    by_p, sig_by_p = by_results[0], by_results[1]
    # by_count = len(sig_by_p)

    # 6 - Qval
    q_results = q_value(p_values, alpha=0.05)
    q, sig_q,pi0_est = q_results[0], q_results[1],q_results[2]
    # q_count = len(sig_q)

    if sigplot == True:
        methods = ['Bonferroni', 'Holm', 'SGoF', 'BH', 'BY', 'Q value']
        sig_indices = [sig_bonf_p, sig_holm_p, sig_sgof_p, sig_bh_p, sig_by_p, sig_q]
        sigindex_plot(methods, sig_indices, title="Significant Index Plot", save_plot = False)

    sig_dict = {
        "Uncorrected": sig_index,
        "Bonferroni": sig_bonf_p,
        "Holm": sig_holm_p,
        "SGoF": sig_sgof_p,
        "BH": sig_bh_p,
        "BY": sig_by_p,
        "Q-value": sig_q,
        "pi0 estimate": pi0_est
    }

    if results == True:
      sig_len_dict = {
        "Uncorrected": len(sig_index),
        "Bonferroni": len(sig_bonf_p),
        "Holm": len(sig_holm_p),
        "SGoF": len(sig_sgof_p),
        "BH": len(sig_bh_p),
        "BY": len(sig_by_p),
        "Q-value": len(sig_q),
        "pi0 estimate": pi0_est
        }
      
      sig_df = pd.DataFrame(sig_len_dict, index=[0])
      print("\n",sig_df, "\n")

    return sig_dict

import random

p_values = [random.uniform(0,1) for i in range(1000)]
multitest(p_values, alpha=0.05, sigplot=True, results = True)
multitest(p_values, alpha=0.05, sigplot=False, results=True)


