from sklearn.neighbors import KNeighborsClassifier
X = [[1, 2], [2, 3], [3, 4], [4, 5]]  
y = [0, 1, 0, 1]  
k = int(input("Enter the value of k (number of neighbors): "))
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X, y)
new_patient_features = [float(input(f"Enter feature {i + 1}: ")) for i in range(len(X[0]))]
prediction = knn_classifier.predict([new_patient_features])
if prediction[0] == 1:
    print("The patient is predicted to have the medical condition.")
else:
    print("The patient is predicted not to have the medical condition.")
