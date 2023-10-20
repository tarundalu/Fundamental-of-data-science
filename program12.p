import pandas as pd
import datetime

# Sample data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [25, 30, 35, 40, 25, 30, 35, 30, 40, 45],
    'purchase_date': ['2023-09-10', '2023-09-15', '2023-09-20', '2023-09-25', '2023-09-05', '2023-09-10', '2023-09-15', '2023-09-20', '2023-09-25', '2023-09-05']
}

# Create a DataFrame
sales_data = pd.DataFrame(data)

# Convert 'purchase_date' to datetime
sales_data['purchase_date'] = pd.to_datetime(sales_data['purchase_date'])

# Filter data for the past month
end_date = datetime.date(2023, 9, 30)
start_date = end_date - datetime.timedelta(days=30)
filtered_data = sales_data[(sales_data['purchase_date'] >= start_date) & (sales_data['purchase_date'] <= end_date)]

# Calculate the frequency distribution of customer ages
age_distribution = filtered_data['age'].value_counts().sort_index()

# Print the result
print(age_distribution)
