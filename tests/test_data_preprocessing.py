import pytest
import pandas as pd
import numpy as np
from customer_segmentation.src.data_preprocessing import clean_data


def test_clean_data_handles_missing_values():
    # Arrange
    data = {
        "feature_1": [1.0, 2.0, np.nan, 4.0],
        "feature_2": [10.0, np.nan, 30.0, 40.0],
    }
    df = pd.DataFrame(data)

    # Act
    cleaned_df = clean_data(df)

    # Assert
    assert not cleaned_df.isnull().values.any(), "Should not contain missing values"
    assert (
        cleaned_df.shape == df.shape
    ), "Cleaned dataframe should have the same dimensions"


def test_clean_data_normalizes_features():
    # Arrange
    data = {
        "feature_1": [1.0, 2.0, 3.0, 4.0],
    }
    df = pd.DataFrame(data)

    # Act
    cleaned_df = clean_data(df)

    # Assert
    # Standard scaler should make the mean approx 0 and std approx 1
    np.testing.assert_almost_equal(cleaned_df["feature_1"].mean(), 0.0, decimal=2)
    np.testing.assert_almost_equal(cleaned_df["feature_1"].std(ddof=0), 1.0, decimal=2)
