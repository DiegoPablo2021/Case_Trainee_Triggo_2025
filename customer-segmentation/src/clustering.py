from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np
from src.logger import get_logger

logger = get_logger(__name__)

class CustomerSegmenter:
    """
    A class to perform customer segmentation and dynamic optimal cluster finding.
    """
    def __init__(self, method: str = "kmeans", max_clusters: int = 10, random_state: int = 42):
        self.method = method
        self.max_clusters = max_clusters
        self.random_state = random_state
        self.model = None
        self.best_k = None
        
    def find_optimal_clusters(self, data: np.ndarray) -> int:
        """
        Dynamically determine the optimal number of clusters using Silhouette Score.
        """
        logger.info("Finding optimal number of clusters using Silhouette Score...")
        best_score = -1.0
        best_k = 2  # Silhouette score requires at least 2 clusters
        
        # We test up to max_clusters, but cap at data size - 1 if smaller
        limit = min(self.max_clusters + 1, data.shape[0])
        
        if limit <= 2:
            logger.warning("Not enough data to calculate silhouette score. Defaulting to 1 cluster (meaningless).")
            return 1

        for k in range(2, limit):
            if self.method == "kmeans":
                model = KMeans(n_clusters=k, random_state=self.random_state)
            elif self.method == "hierarchical":
                model = AgglomerativeClustering(n_clusters=k)
            else:
                raise ValueError("Unsupported clustering method under optimal search.")
            
            labels = model.fit_predict(data)
            score = silhouette_score(data, labels)
            logger.info(f"k={k} -> Silhouette Score = {score:.4f}")
            
            if score > best_score:
                best_score = score
                best_k = k
                
        logger.info(f"Optimal number of clusters found: k={best_k} (Score: {best_score:.4f})")
        return best_k

    def perform_clustering(self, data: np.ndarray, n_clusters: int = None) -> np.ndarray:
        """
        Perform clustering on the data. Uses dynamic k if n_clusters isn't given.
        """
        if data.size == 0:
            logger.error("Input data for clustering is empty.")
            raise ValueError("Input DataFrame is empty.")

        if n_clusters is None:
            self.best_k = self.find_optimal_clusters(data)
            n_clusters = self.best_k
        else:
            self.best_k = n_clusters
            logger.info(f"Using exactly requested {n_clusters} clusters.")
            
        if self.method == "kmeans":
            logger.info(f"Running KMeans with {n_clusters} clusters.")
            self.model = KMeans(n_clusters=n_clusters, random_state=self.random_state)
            cluster_labels = self.model.fit_predict(data)
        elif self.method == "hierarchical":
            logger.info(f"Running AgglomerativeClustering with {n_clusters} clusters.")
            self.model = AgglomerativeClustering(n_clusters=n_clusters)
            cluster_labels = self.model.fit_predict(data)
        else:
            logger.error(f"Unsupported clustering method: {self.method}")
            raise ValueError("Unsupported clustering method. Choose 'kmeans' or 'hierarchical'.")

        logger.info("Clustering completed successfully.")
        return cluster_labels


# Backward compatible function wrappers
def perform_clustering(
    data: pd.DataFrame, method: str = "kmeans", n_clusters: int = 3
) -> np.ndarray:
    logger.info(f"[Legacy] Running perform_clustering with {method}, k={n_clusters}")
    segmenter = CustomerSegmenter(method=method)
    return segmenter.perform_clustering(data, n_clusters=n_clusters)