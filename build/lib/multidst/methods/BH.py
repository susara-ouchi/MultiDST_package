#loading p values
#from A01_sim_data import p_values, fire_index, nonfire_index
from statsmodels.stats.multitest import multipletests

def bh_method(p_values, alpha=0.05):
    #from statsmodels.stats.multitest import multipletests
    # Apply BH correction
    adj_p = multipletests(p_values, method='fdr_bh')[1]
    sig_index = [index for index,p in enumerate(adj_p) if p < alpha]
    return adj_p, sig_index

p_values = [0.0001,0.05,0.3]
bh_results = bh_method(p_values,alpha=0.05)
bh_p, sig_bh_p = bh_results[0], bh_results[1]
bh_p
sig_bh_p
