import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 15000, 11000, 14000, 16000]
plt.plot(months, sales, marker='o', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Over Time')
plt.show()
plt.scatter(months, sales, marker='o', color='blue')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Scatter Plot')
plt.show()
plt.bar(months, sales, color='green')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Bar Plot')
plt.show()
