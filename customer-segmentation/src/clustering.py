from sklearn.cluster import KMeans, AgglomerativeClustering
import pandas as pd

def perform_clustering(data, method='kmeans', n_clusters=3):
    if method == 'kmeans':
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(data)
    elif method == 'hierarchical':
        hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
        cluster_labels = hierarchical.fit_predict(data)
    else:
        raise ValueError("Unsupported clustering method. Choose 'kmeans' or 'hierarchical'.")
    
    return cluster_labels