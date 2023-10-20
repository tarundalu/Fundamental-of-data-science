import numpy as np
import pandas as pd
from scipy import stats
np.random.seed(0)
synthetic_data = np.random.normal(loc=10, scale=2, size=100)
sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95% confidence): "))
desired_precision = float(input("Enter the desired level of precision: "))
sample = np.random.choice(synthetic_data, size=sample_size, replace=False)
sample_mean = np.mean(sample)
std_error = stats.sem(sample)
z_score = stats.norm.ppf((1 + confidence_level) / 2)
margin_of_error = z_score * (std_error / np.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(f"Sample Mean: {sample_mean}")
print(f"Margin of Error: {margin_of_error}")
print(f"Confidence Interval: {confidence_interval}")
