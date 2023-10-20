from sklearn.linear_model import LinearRegression


X = [[1200, 3], [1400, 2], [1600, 3], [1800, 4]]  
y = [250000, 300000, 320000, 400000]  

linear_regression_model = LinearRegression()
linear_regression_model.fit(X, y)


new_house_area = float(input("Enter the area of the new house: "))
new_house_bedrooms = int(input("Enter the number of bedrooms in the new house: "))


new_house_features = [[new_house_area, new_house_bedrooms]]


predicted_price = linear_regression_model.predict(new_house_features)

print(f"The predicted price of the new house is: ${predicted_price[0]:,.2f}")
