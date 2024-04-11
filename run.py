from multidst.functions import multitest
import random

from multidst.utils.visualization import sigindex_plot

# Create p_values
p_values = [random.uniform(0,0.03) for i in range(1000)]


# Carrying out MultiDST for a list of p_values
# multitest(p_values, alpha=0.05,sigplot=True)

# Carrying out MultiDST for a list of IHW p_values
from multidst.utils.weighting import weighted_p_list
random.seed(2)
weights =  [random.uniform(0,1) for i in range(1000)]
weighted_p_list(p_values, weights=weights)

# multitest(p_values, alpha=0.05, sigplot=True)

# Carrying out MultiDST under Multi-weighting
from multidst.utils.weighting import weighted_p_list
weighting = 1

p_values = [random.uniform(0,0.03) for i in range(1000)]
weighted_p_list(p_values, weights="multi",max_weight=1.5, min_weight = 0.5)

len(p_values)