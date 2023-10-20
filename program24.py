import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv('dataset.csv')


features = input("Enter the names of the features (separated by comma): ").split(',')
target_variable = input("Enter the name of the target variable: ")

# Split the dataset into features and target variable
X = dataset[features]
y = dataset[target_variable]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a machine learning model
model = LogisticRegression()
model.fit(X_train, y_train)
