from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_clusters(data, cluster_labels):
    data['Cluster'] = cluster_labels
    cluster_summary = data.groupby('Cluster').mean().reset_index()
    return cluster_summary

def visualize_clusters(data, cluster_labels):
    data['Cluster'] = cluster_labels
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='total_pedidos', y='ticket_medio', hue='Cluster', data=data, palette='Set2', alpha=0.7)
    plt.title('Segmentação de Clientes por Clusters')
    plt.xlabel('Total de Pedidos')
    plt.ylabel('Ticket Médio')
    plt.legend(title='Cluster')
    plt.tight_layout()
    plt.show()