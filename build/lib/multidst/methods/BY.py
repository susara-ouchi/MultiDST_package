from statsmodels.stats.multitest import multipletests

def BY_method(p_values, alpha=0.05, weights = None):
    """
    Applies the Benjamini-Yekutieli (BY) method for controlling the False Discovery Rate (FDR) 
    from the `statsmodels.stats.multitest` package.

    Parameters:
    - p_values (list of float): List of p-values to be corrected.
    - alpha (float, optional): Significance threshold. Default is 0.05.
    - weights (list of float, optional): Not used in this method. Included for consistency with other methods.

    Returns:
    - adj_p (list of float): List of adjusted p-values after applying the BY correction.
    - sig_index (list of int): List of indices of significant p-values after the BY correction.
    """
    adj_p = multipletests(p_values, method='fdr_by')[1]
    sig_index = [index for index,p in enumerate(adj_p) if p < alpha]
    
    return adj_p, sig_index


p_values = [0,0.1,0.2,0.003]

by_results = BY_method(p_values,alpha=0.05, weights = None)
by_p, sig_by_p = by_results[0], by_results[1]
by_p
sig_by_p
len(sig_by_p)
