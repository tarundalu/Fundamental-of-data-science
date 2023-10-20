import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


customer_data = pd.read_csv('customer_data.csv')

features = ['purchase_history', 'browsing_behavior', 'age', 'gender']


scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data[features])


pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)


kmeans = KMeans(n_clusters=4)
kmeans.fit(reduced_data)


customer_data['cluster'] = kmeans.labels_

plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans.labels_)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Customer Segmentation')
plt.show()


print("Customer Segmentation:")
print(customer_data[['customer_id', 'cluster']])
