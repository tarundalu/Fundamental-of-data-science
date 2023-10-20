import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Read customer data from a CSV file into a Pandas DataFrame
customer_data = pd.read_csv('customer_data.csv')

# Select the relevant shopping-related features for clustering
features = ['age', 'income', 'purchase_frequency']

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_data[features])

# Perform K-means clustering
n_clusters = 3  # Change this value according to the number of desired clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(scaled_features)

# Get the cluster labels
cluster_labels = kmeans.labels_

# Assign a new customer to a cluster based on their input features
new_customer = []  # Enter the shopping-related features of the new customer here
scaled_new_customer = scaler.transform([new_customer])
cluster = kmeans.predict(scaled_new_customer)[0]

# Print the assigned cluster for the new customer
print(f"The new customer is assigned to Cluster {cluster}.")
