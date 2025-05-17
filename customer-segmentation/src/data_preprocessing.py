import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load customer data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """Clean the customer data by handling missing values and normalizing."""
    # Handle missing values
    df.fillna(df.mean(), inplace=True)
    
    # Normalize numerical features
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df

def prepare_data(file_path):
    """Load and clean the customer data."""
    df = load_data(file_path)
    df = clean_data(df)
    return df