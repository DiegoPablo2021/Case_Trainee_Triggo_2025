import pytest
import pandas as pd
import numpy as np
import os
from src.data_preprocessing import CustomerDataProcessor

@pytest.fixture
def sample_data_path(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_data.csv"
    p.write_text("id,val1,val2\n1,10.0,20.0\n2,,30.0\n3,40.0,")
    return p

def test_load_data_success(sample_data_path):
    processor = CustomerDataProcessor()
    df = processor.load_data(sample_data_path)
    assert not df.empty
    assert len(df) == 3

def test_load_data_file_not_found():
    processor = CustomerDataProcessor()
    with pytest.raises(FileNotFoundError):
        processor.load_data("non_existent_file.csv")

def test_clean_data(sample_data_path):
    processor = CustomerDataProcessor()
    df = processor.load_data(sample_data_path)
    df_clean = processor.clean_data(df)
    
    # Missing values should be imputed
    assert not df_clean.isnull().any().any()
    
    # Data should be scaled (mean close to 0)
    assert np.isclose(df_clean['val1'].mean(), 0, atol=1e-7)
    assert np.isclose(df_clean['val2'].mean(), 0, atol=1e-7)

def test_clean_data_empty():
    processor = CustomerDataProcessor()
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        processor.clean_data(df)
