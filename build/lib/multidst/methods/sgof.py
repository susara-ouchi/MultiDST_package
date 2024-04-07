import numpy as np
from scipy.stats import chi2

def sgof_test(p_values, alpha):
    # Step 01: Sort p-values in ascending order
    sorted_p_values = np.sort(p_values)
    
    # Step 02: Initialize R (number of p-values below threshold)
    R = np.sum(sorted_p_values <= alpha)
    
    # Step 03: Test if observed discoveries deviate significantly
    while R > 0:
        # Perform chi-square test
        observed = R
        #print(observed)
        expected = len(sorted_p_values) * alpha
        chi_square_statistic = (observed - expected) ** 2 / expected
        p_value_chi2 = 1 - chi2.cdf(chi_square_statistic, df=1)  # df=1 for chi-square

        # Check significance
        if p_value_chi2 < alpha:
            R -= 1
        else:
            break
    
    # Step 04: Extract significant tests and their indices
    significant_tests = sorted_p_values[:R]
    significant_indices = np.where(np.isin(p_values, significant_tests))[0]

    significant_tests = significant_tests.tolist()
    significant_indices = significant_indices.tolist()

    return significant_tests, significant_indices

p_values = [0.0003,0.01,0.4,0.02,0.0003]

sgof_results = sgof_test(p_values,alpha=0.05)
sgof_p, sig_sgof_p = sgof_results[0], sgof_results[1]
sgof_p
sig_sgof_p
len(sig_sgof_p)
len(sgof_p)
