import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def run_kmeans(data_path, n_clusters=5):
    data = pd.read_csv(data_path)
    X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    
    data['Cluster'] = clusters
    
    sns.scatterplot(
        x='Annual Income (k$)',
        y='Spending Score (1-100)',
        hue='Cluster',
        data=data,
        palette='Set1'
    )
    plt.title('Customer Segments')
    plt.show()
    
    return data

if __name__ == "__main__":
    result = run_kmeans(r"C:\Users\bsneh\OneDrive\Desktop\ml\Mall_Customers.csv")

    print(result.head())
    print(result['Cluster'].value_counts())
