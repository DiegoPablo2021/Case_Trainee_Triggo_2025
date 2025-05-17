def plot_cluster_distribution(cluster_labels):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.countplot(x=cluster_labels, palette='viridis')
    plt.title('Distribution of Customer Clusters')
    plt.xlabel('Cluster Label')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def calculate_silhouette_score(X, cluster_labels):
    from sklearn.metrics import silhouette_score
    return silhouette_score(X, cluster_labels)

def save_to_csv(data, filename):
    data.to_csv(filename, index=False)

def load_from_csv(filename):
    import pandas as pd
    return pd.read_csv(filename)