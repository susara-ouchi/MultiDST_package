#loading p values
#from A01_sim_data import p_values, fire_index, nonfire_index
from statsmodels.stats.multitest import multipletests

def bh_method(p_values, alpha=0.05):
    """
    Applies the Benjamini-Hochberg (BH) method for controlling the False Discovery Rate (FDR) from the `statsmodels.stats.multitest` package.

    Parameters:
    - p_values (list of float): List of p-values to be corrected.
    - alpha (float, optional): Significance threshold. Default is 0.05.

    Returns:
    - adj_p (list of float): List of adjusted p-values after applying the BH correction.
    - sig_index (list of int): List of indices of significant p-values after the BH correction.
    """
    adj_p = multipletests(p_values, method='fdr_bh')[1]
    sig_index = [index for index,p in enumerate(adj_p) if p < alpha]
    return adj_p, sig_index

p_values = [0.0001,0.05,0.3]
bh_results = bh_method(p_values,alpha=0.05)
bh_p, sig_bh_p = bh_results[0], bh_results[1]
bh_p
sig_bh_p
