from statsmodels.stats.multitest import multipletests

#Define function for Holm Procedure 
import numpy as np

def holm(p_values, alpha=0.05):
    # from statsmodels.stats.multitest import multipletests
    # Apply Holm-Bonferroni correction
    adj_p = multipletests(p_values, method='holm')[1]
    sig_index = [index for index,p in enumerate(adj_p) if p < alpha]
        
    return adj_p, sig_index

p_values = [0.0005279804659690256, 0.0005107595122255753, 0.005380747546894805, 0.008293070676726721, 0.015261930084251897, 0.09399292181095295, 0.04916062506442831, 0.08455877419751781, 0.026622720150619863, 0.060671184302609794, 0.014792473316734833, 0.029279038132892888, 0.039948575984906864, 0.05455860141093238, 0.06495646577203158, 0.01393407242591071, 0.06592036470024257, 0.03370049417508525, 0.08285377432610773, 0.055087308119778314]
holm_results = holm(p_values,alpha=0.05)
holm_p, sig_holm_p = holm_results[0], holm_results[1]
holm_p
sig_holm_p
