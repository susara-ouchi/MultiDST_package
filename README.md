# MultiDST Package

" MultiDST - Multiple Testing Made Easy"

The MultiDST Package is a Python library designed for multiple hypothesis testing in statistical analysis. It provides implementations of various methods to control the family-wise error rate (FWER) and false discovery rate (FDR) in scenarios involving multiple hypothesis tests.
Significant Index Plot (SIP) can be used to visualize the significant hypotheses under each of the method with ease.

## Implemented Methods

    Bonferroni Correction
        Reason for Selection: Baseline method; simple and conservative.
        Error Type: Controls the family-wise error rate (FWER).
        Reference: Bonferroni, C. (1935). Il calcolo delle assicurazioni su gruppi di teste. https://api.semanticscholar.org/CorpusID:89994272

    Holm-Bonferroni Correction
        Reason for Selection: Sequential approach; adjusts thresholds progressively.
        Error Type: Controls the family-wise error rate (FWER).
        Reference: Holm, S. (1979). A Simple Sequentially Rejective Multiple Test Procedure. Source: Scandinavian Journal of Statistics Scand J Statist, 6(6), 65–70. http://www.jstor.org/stable/4615733%0Ahttp://www.jstor.org/page/info/about/policies/terms.jsp%0Ahttp://www.jstor.org

    Benjamini-Hochberg Procedure
        Reason for Selection: Balances power and control; widely used in genomics.
        Error Type: Controls the false discovery rate (FDR).
        Reference: Benjamini, Y., & Hochberg, Y. (1995). "Controlling the false discovery rate: A practical and powerful approach to multiple testing." Journal of the Royal Statistical Society. Series B (Methodological), 57(1), 289-300.

    Benjamini-Yekutieli Method
        Reason for Selection: FDR control under dependence; accounts for correlated tests.
        Error Type: Controls the false discovery rate (FDR).
        Reference: Benjamini, Y., & Yekutieli, D. (2001a). The control of the false discovery rate in multiple testing under dependency. Annals of Statistics, 29(4), 1165–1188. https://doi.org/10.1214/aos/1013699998

    Storey’s Q Value
        Reason for Selection: Adaptive FDR control; estimates proportion of true null hypotheses.
        Error Type: Controls the false discovery rate (FDR).
        Reference: Storey, J. D., & Tibshirani, R. (2003). Statistical Significance for Genome-Wide Studies.

    SGoF Test (Sequential Goodness-of-Fit)
        Reason for Selection: Increased power for large-scale testing; combines p-values from multiple tests.
        Error Type: Varies (depends on setup).
        Reference: Carvajal-Rodríguez, A., de Uña-Alvarez, J., & Rolán-Alvarez, E. (2009). A new multitest correction (SGoF) that increases its statistical power when increasing the number of tests. BMC Bioinformatics, 10, 209. https://doi.org/10.1186/1471-2105-10-209

## Installation
You can install the MultiDST Package using pip:

```bash
pip install MultiDST_package
```

## Special Features
    Multiple Methods: Implements several established methods for multiple hypothesis testing, including Bonferroni correction, Holm-Bonferroni correction, Benjamini-Hochberg procedure, and more.

    Flexible Usage: Designed to handle different types of data and scenarios typically encountered in statistical analysis.

    Integration: Methods are integrated into a unified framework, making it easier to apply and compare different approaches within the same analysis.

    Enhancements: Includes novel enhancements such as a "hybrid" procedure and "multi-weighting" to improve robustness and flexibility in hypothesis testing.

    Visualization: Provides tools for visualizing significant hypotheses, aiding in the interpretation of results.
