import numpy as np
sales_data = np.array([25000, 30000, 28000,32000])
total_sales = np.sum(sales_data)
ql_sales = sales_data[0]
q4_sales = sales_data[3]
percentage_increase = ((q4_sales - ql_sales) / ql_sales) * 100
print (f"Total Sales for the Year: ${total_sales}")
print (f"Percentage Increase from Q1 to Q4: {percentage_increase:.2f}%")

