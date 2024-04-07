from statsmodels.stats.multitest import multipletests

def BY_method(p_values, alpha=0.05, weights = None):
    # from statsmodels.stats.multitest import multipletests
    # Apply Benjamini-Yekutieli correction
    adj_p = multipletests(p_values, method='fdr_by')[1]
    sig_index = [index for index,p in enumerate(adj_p) if p < alpha]
    
    return adj_p, sig_index


p_values = [0,0.1,0.2,0.003]

by_results = BY_method(p_values,alpha=0.05, weights = None)
by_p, sig_by_p = by_results[0], by_results[1]
by_p
sig_by_p
len(sig_by_p)
