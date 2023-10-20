import pandas as pd
import numpy as np


stock_data = pd.read_csv('stock_data.csv')


stock_data['Price Change'] = stock_data['Close'].diff()


stock_data['Percentage Change'] = stock_data['Price Change'] / stock_data['Close'].shift() * 100

volatility = np.std(stock_data['Percentage Change'])
mean_percentage_change = np.mean(stock_data['Percentage Change'])


if volatility < 1:
    volatility_level = 'Low'
elif volatility < 2:
    volatility_level = 'Moderate'
else:
    volatility_level = 'High'

if mean_percentage_change > 0:
    direction = 'upward'
else:
    direction = 'downward'

print(f"The stock's price movements are characterized by {volatility_level} volatility.")
print(f"The average daily percentage change indicates an {direction} trend.")
