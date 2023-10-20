from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


iris = load_iris()
X = iris.data  
y = iris.target 


decision_tree_classifier = DecisionTreeClassifier(random_state=42)
decision_tree_classifier.fit(X, y)


sepal_length = float(input("Enter sepal length (cm): "))
sepal_width = float(input("Enter sepal width (cm): "))
petal_length = float(input("Enter petal length (cm): "))
petal_width = float(input("Enter petal width (cm): "))


new_flower_features = [[sepal_length, sepal_width, petal_length, petal_width]]

predicted_species = decision_tree_classifier.predict(new_flower_features)


species_names = {0: "setosa", 1: "versicolor", 2: "virginica"}

predicted_species_name = species_names[predicted_species[0]]
print(f"The predicted species is: {predicted_species_name}")
