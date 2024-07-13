from multidst.functions import multitest
import random

### Everything to do 

# Create p_values
p_values = [random.uniform(0,0.03) for i in range(1000)]

# Carrying out MultiDST for a list of p_values
multitest(p_values, alpha=0.05,sigplot=True)

# Carrying out MultiDST for a list of IHW p_values
from multidst.utils.weighting import weighted_p_list
random.seed(2)
weights =  [random.uniform(0,1) for i in range(1000)]
weighted_p_list(p_values, weights=weights)

# Carrying out MultiDST under Multi-weighting
from multidst.utils.weighting import weighted_p_list
weighting = weighted_p_list(p_values, weights="multi",max_weight=1.5, min_weight = 0.5)
weighting[0]


### Visualizations & Results 

# Getting results - this sigplot is not going to be saved (it is defined in the code to not save)
multitest(p_values, alpha=0.05, sigplot=True)


# Code to draw and save the sig plot
from multidst.utils.visualization import sigindex_plot
methods = ['Bonferroni', 'Holm', 'SGoF', 'BH', 'BY', 'Q value']
res = multitest(p_values, alpha=0.05, sigplot=True)
sig_indices = [res['Bonferroni'], res['Holm'], res['SGoF'], res['BH'], res['BY'], res['Q-value']]
sigindex_plot(methods,sig_indices,title="Significant index plot")

# Code for the histogram - this is saved by default
from multidst.utils.visualization import multidst_hist
p_values = [random.uniform(0,0.5) for i in range(1000)]
g2_index = []
multidst_hist(p_values, g2_index, title="Histogram of p-values",col1 = 'skyblue', col2 = 'purple')

p_values = [0.1,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
g2_index = [2,5,9,10]
multidst_hist(p_values,g2_index, title="Histogram",col1 = 'skyblue', col2 = 'purple', show_legend=True, left='Original',right='Group 02')

### Issue: Plots are not getting saved properly!! Why is it a white box
