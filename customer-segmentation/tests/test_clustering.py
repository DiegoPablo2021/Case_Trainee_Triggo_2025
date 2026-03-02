import pytest
import numpy as np
from src.clustering import CustomerSegmenter

@pytest.fixture
def mock_data():
    np.random.seed(42)
    # Generate 3 distinct blobs of data
    d1 = np.random.normal(loc=0, scale=0.5, size=(50, 2))
    d2 = np.random.normal(loc=5, scale=0.5, size=(50, 2))
    d3 = np.random.normal(loc=10, scale=0.5, size=(50, 2))
    return np.vstack((d1, d2, d3))

def test_find_optimal_clusters(mock_data):
    segmenter = CustomerSegmenter(max_clusters=5)
    best_k = segmenter.find_optimal_clusters(mock_data)
    assert best_k == 3 # the data naturally has 3 distinct blobs

def test_perform_clustering_dynamic(mock_data):
    segmenter = CustomerSegmenter(max_clusters=5)
    labels = segmenter.perform_clustering(mock_data)
    assert len(labels) == len(mock_data)
    # Should identify 3 unique labels
    assert len(np.unique(labels)) == 3

def test_perform_clustering_explicit(mock_data):
    segmenter = CustomerSegmenter()
    labels = segmenter.perform_clustering(mock_data, n_clusters=4)
    assert len(np.unique(labels)) == 4

def test_perform_clustering_empty():
    segmenter = CustomerSegmenter()
    with pytest.raises(ValueError):
        segmenter.perform_clustering(np.array([]))
