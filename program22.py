from sklearn.linear_model import LogisticRegression

# Example dataset (replace this with your own dataset)
X = [[300, 12], [600, 24], [200, 6], [800, 36]]  # Features (usage minutes, contract duration)
y = [1, 0, 1, 0]  # Churn status (1 for churned, 0 for not churned)

# Train a Logistic Regression model
logistic_regression_model = LogisticRegression(random_state=42)
logistic_regression_model.fit(X, y)

# Input features for a new customer
new_customer_usage = int(input("Enter usage minutes for the new customer: "))
new_customer_contract_duration = int(input("Enter contract duration for the new customer: "))

# Create a feature array for the new customer
new_customer_features = [[new_customer_usage, new_customer_contract_duration]]

# Predict churn status for the new customer
predicted_churn = logistic_regression_model.predict(new_customer_features)

if predicted_churn[0] == 1:
    print("The new customer is predicted to churn.")
else:
    print("The new customer is predicted not to churn.")
