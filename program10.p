import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [10, 12, 15, 18, 20, 22]
plt.plot(months, temperature, marker='o', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Data')
plt.show()
rainfall = [50, 40, 60, 30, 70, 55]
plt.scatter(months, rainfall, marker='o', color='blue')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Data')
plt.show()
