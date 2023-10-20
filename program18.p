import pandas as pd
import numpy as np
import scipy.stats as stats

# Generate example data (replace with your actual data)
np.random.seed(42)
ratings_data = pd.DataFrame({
    'product_category': ['Electronics'] * 100,  # Category for demonstration
    'rating': np.random.randint(1, 6, 100)  # Example ratings between 1 and 5
})

# Specify the product category you want to analyze
selected_category = "Electronics"

# Filter the data for the selected category
selected_data = ratings_data[ratings_data["product_category"] == selected_category]

# Set the confidence level (e.g., 95% confidence)
confidence_level = 0.95

# Calculate the sample size and mean rating
sample_size = len(selected_data)
sample_mean = selected_data["rating"].mean()

# Calculate the standard error of the mean
standard_error = selected_data["rating"].std() / np.sqrt(sample_size)

# Calculate the critical value (t) for the confidence level
t_critical = stats.t.ppf(1 - (1 - confidence_level) / 2, df=sample_size - 1)

# Calculate the margin of error
margin_of_error = t_critical * standard_error


lower_limit = sample_mean - margin_of_error
upper_limit = sample_mean + margin_of_error

print(f"Product Category: {selected_category}")
print(f"Sample Size: {sample_size}")
print(f"Sample Mean Rating: {sample_mean:.2f}")
print(f"Confidence Interval: ({lower_limit:.2f}, {upper_limit:.2f})")
