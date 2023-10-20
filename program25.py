import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing


data = pd.read_csv('car_data.csv')


mileage = int(input("Enter the mileage of the new car: "))
age = int(input("Enter the age of the new car: "))
brand = input("Enter the brand of the new car: ")
engine_type = input("Enter the engine type of the new car: ")


le = preprocessing.LabelEncoder()
brand = le.fit_transform([brand])
engine_type = le.fit_transform([engine_type])


new_car = pd.DataFrame([[mileage, age, brand[0], engine_type[0]]], columns=['mileage', 'age', 'brand', 'engine_type'])


X = data[['mileage', 'age', 'brand', 'engine_type']]
y = data['price']


cart = DecisionTreeRegressor()


cart.fit(X, y)


predicted_price = cart.predict(new_car)


decision_path = cart.decision_path(new_car)


print("The predicted price of the new car is $", predicted_price[0])


print("Decision path:")
for node_id in decision_path.indices:
    feature = cart.tree_.feature[node_id]
    threshold = cart.tree_.threshold[node_id]
    if feature != -2:
        print("If", X.columns[feature], "<=", threshold, "then go to left node")
    else:
        print("Predicted price")
