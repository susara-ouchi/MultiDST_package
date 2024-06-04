from multidst.functions import multitest
import random

# Create p_values
p_values = [random.uniform(0,0.03) for i in range(1000)]

# Carrying out MultiDST for a list of p_values
multitest(p_values, alpha=0.05,sigplot=True)

# Carrying out MultiDST for a list of IHW p_values
from multidst.utils.weighting import weighted_p_list
random.seed(2)
weights =  [random.uniform(0,1) for i in range(1000)]
weighted_p_list(p_values, weights=weights)

multitest(p_values, alpha=0.05, sigplot=True)

# Carrying out MultiDST under Multi-weighting
from multidst.utils.weighting import weighted_p_list
weighting = weighted_p_list(p_values, weights="multi",max_weight=1.5, min_weight = 0.5)
weighting[0]

from multidst.utils.visualization import multidst_hist
p_values = [random.uniform(0,0.5) for i in range(1000)]
g2_index = []
multidst_hist(p_values, g2_index, title="Histogram of p-values",col1 = 'skyblue', col2 = 'purple')

p_values = [0.1,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
g2_index = [2,5,9,10]
multidst_hist(p_values,g2_index, title="Histogram",col1 = 'skyblue', col2 = 'purple', show_legend=True, left='Original',right='Group 02')

