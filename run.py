
from .multidst.functions import multi_DST
import random

# Carrying out MultiDST for a list of p_values
p_values = [random.uniform(0,100) for i in range(100)]
multi_DST(p_values, alpha=0.05)

# Carrying out MultiDST for a list of weighted p_values
from utils.weighting import weighted_p_list
weights =  [random.uniform(0,100) for i in range(100)]
p_values = [random.uniform(0,1) for i in range(100)]
weighted_p_list(p_values, weights=weights)
multi_DST(p_values, alpha=0.05)

# Carrying out MultiDST under Multi-weighting
from utils.weighting import weighted_p_list
weights =  [random.uniform(0,100) for i in range(100)]
p_values = [random.uniform(0,1) for i in range(100)]
weighted_p_list(p_values, weights=weights)
multiDST_res = multi_DST(p_values, alpha=0.05)
multiDST_res['Uncorrected']

sig_bonf_p, sig_holm_p, sig_sgof_p, sig_bh_p, sig_by_p, sig_q = multiDST_res['Bonferroni'],multiDST_res['Holm'],multiDST_res['SGoF'],multiDST_res['BH'],multiDST_res['BY'], multiDST_res['Q-value']


import numpy as np
from utils.common_indices import common_indices

p_values = np.random.random(22)

sig_bonf_p, sig_holm_p, sig_sgof_p, sig_bh_p, sig_by_p, sig_q = multiDST_res['Bonferroni'],multiDST_res['Holm'],multiDST_res['SGoF'],multiDST_res['BH'],multiDST_res['BY'], multiDST_res['Q-value']
coms = common_indices(p_values,sig_bonf_p, sig_holm_p, sig_sgof_p, sig_bh_p, sig_by_p, sig_q)

l0, l1, l2, l3, l4, l5, l6 = coms[0],coms[1],coms[2],coms[3],coms[4],coms[5],coms[6]
weighting = weighted_p_list(p_values, l0, l1, l2, l3, l4, l5, l6, weights="multi")