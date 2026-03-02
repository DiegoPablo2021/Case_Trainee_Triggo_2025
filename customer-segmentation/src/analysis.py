import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.logger import get_logger

logger = get_logger(__name__)


def analyze_clusters(data: pd.DataFrame, cluster_labels: np.ndarray) -> pd.DataFrame:
    """
    Analyze the resulting clusters by computing the mean of features for each cluster.
    """
    if data.empty:
        logger.error("Input data is empty. Cannot analyze clusters.")
        raise ValueError("Data is empty.")
    
    if len(data) != len(cluster_labels):
        logger.error("Length mismatch between data and cluster labels.")
        raise ValueError("Length mismatch between data and cluster labels.")
        
    logger.info("Analyzing cluster groupings...")
    data_with_clusters = data.copy()
    data_with_clusters["Cluster"] = cluster_labels
    cluster_summary = data_with_clusters.groupby("Cluster").mean().reset_index()
    logger.info("Cluster analysis completed.")
    return cluster_summary


def visualize_clusters(data: pd.DataFrame, cluster_labels: np.ndarray) -> None:
    """
    Visualize the customer segments using a scatter plot.
    """
    if data.empty:
        logger.warning("Empty data provided. Skipping visualization.")
        return
        
    logger.info("Generating cluster visualization...")
    data_with_clusters = data.copy()
    data_with_clusters["Cluster"] = cluster_labels
    
    # We require specific columns for the plot, so we robustly check them
    if "total_pedidos" not in data.columns or "ticket_medio" not in data.columns:
        logger.warning("Missing columns 'total_pedidos' or 'ticket_medio' for plotting. Plotting first two features instead.")
        x_col = data.columns[0]
        y_col = data.columns[1] if len(data.columns) > 1 else data.columns[0]
    else:
        x_col = "total_pedidos"
        y_col = "ticket_medio"
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=x_col,
        y=y_col,
        hue="Cluster",
        data=data_with_clusters,
        palette="Set2",
        alpha=0.7,
    )
    plt.title("Segmentação de Clientes por Clusters")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend(title="Cluster")
    plt.tight_layout()
    plt.show()
    logger.info("Visualization generated.")