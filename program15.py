import numpy as np
import scipy.stats as stats
drug_group_data = [5, 8, 7, 6, 7, 9, 6, 5, 7, 8, 5, 6, 6, 9, 8, 7, 6, 7, 5, 8, 9, 7, 5, 6, 7, 8, 6, 9, 8, 7]
placebo_group_data = [2, 3, 1, 4, 3, 2, 4, 2, 3, 4, 1, 2, 3, 3, 4, 2, 1, 3, 2, 4, 1, 2, 3, 4, 2, 3, 1, 2, 3, 4]
mean_drug = np.mean(drug_group_data)
std_error_drug = stats.sem(drug_group_data)
conf_int_drug = stats.t.interval(0.95, len(drug_group_data) - 1, loc=mean_drug, scale=std_error_drug)
mean_placebo = np.mean(placebo_group_data)
std_error_placebo = stats.sem(placebo_group_data)
conf_int_placebo = stats.t.interval(0.95, len(placebo_group_data) - 1, loc=mean_placebo, scale=std_error_placebo)
print("95% Confidence Interval for Drug Group Mean Reduction:", conf_int_drug)
print("95% Confidence Interval for Placebo Group Mean Reduction:", conf_int_placebo)
