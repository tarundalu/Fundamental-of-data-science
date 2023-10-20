import scipy.stats as stats
conversion_rate_design_A = [0.10, 0.12, 0.15, 0.09, 0.11, 0.13, 0.12, 0.10, 0.14, 0.10]
conversion_rate_design_B = [0.10, 0.13, 0.14, 0.12, 0.10, 0.12, 0.11, 0.13, 0.14, 0.12]
t_stat, p_value = stats.ttest_ind(conversion_rate_design_A, conversion_rate_design_B)
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference between website design A and B.")
else:
    print("There is no statistically significant difference between website design A and B.")
