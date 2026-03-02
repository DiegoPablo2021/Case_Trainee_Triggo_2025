import pytest
import pandas as pd
import numpy as np
from customer_segmentation.src.clustering import perform_clustering


def test_perform_clustering_kmeans():
    # Arrange
    np.random.seed(42)
    data = pd.DataFrame(np.random.rand(10, 3), columns=["f1", "f2", "f3"])
    n_clusters = 2

    # Act
    labels = perform_clustering(data, method="kmeans", n_clusters=n_clusters)

    # Assert
    assert len(labels) == 10
    assert len(np.unique(labels)) == n_clusters


def test_perform_clustering_hierarchical():
    # Arrange
    np.random.seed(42)
    data = pd.DataFrame(np.random.rand(10, 3), columns=["f1", "f2", "f3"])
    n_clusters = 3

    # Act
    labels = perform_clustering(data, method="hierarchical", n_clusters=n_clusters)

    # Assert
    assert len(labels) == 10
    assert len(np.unique(labels)) == n_clusters


def test_perform_clustering_invalid_method():
    # Arrange
    data = pd.DataFrame(np.random.rand(5, 2))

    # Act & Assert
    with pytest.raises(ValueError, match="Unsupported clustering method"):
        perform_clustering(data, method="invalid_algorithm")
