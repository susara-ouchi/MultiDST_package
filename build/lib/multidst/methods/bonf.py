def bonferroni(p_values, alpha=0.05):
    '''
    Apply Bonferroni correction to a vector of p-values.

    Parameters:
        p_values (list or numpy array): Vector of original p-values.
        alpha: Threshold of significance
        weights: List of input weights

    Returns:
        corrected_p_values(list): Vector of corrected p-values after Bonferroni correction.
    '''
    # Apply Bonferroni correction to each raw p-value
    adj_p = [min(p * len(p_values), 1.0) for p in p_values]
    sig_index = [index for index,p in enumerate(adj_p) if p < alpha]
    
    return adj_p, sig_index
