import pandas as pd
import numpy as np
h=pd.read_csv("Housing.csv")
arr=np.array(h)
price=h["price"]
bedroom=h["bedrooms"]
avg=np.mean(price[bedroom>3])
print(avg)
