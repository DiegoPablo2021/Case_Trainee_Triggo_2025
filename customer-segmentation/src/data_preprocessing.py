import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Union
from pathlib import Path
from src.logger import get_logger

logger = get_logger(__name__)

class CustomerDataProcessor:
    """
    A class used to process and clean customer datasets.
    It maintains state, such as the fitted StandardScaler, allowing for
    consistent transformations across train/test sets or new data.
    """
    def __init__(self):
        self.scaler = StandardScaler()
        self._is_fitted = False
        
    def load_data(self, file_path: Union[str, Path]) -> pd.DataFrame:
        """
        Load customer data from a CSV file with robust error handling.
        """
        try:
            logger.info(f"Loading data from {file_path}")
            df = pd.read_csv(file_path)
            if df.empty:
                logger.warning(f"File {file_path} loaded successfully but is empty.")
            else:
                logger.info(f"Data loaded with shape {df.shape}")
            return df
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}. Please check the path.")
            raise
        except pd.errors.EmptyDataError:
            logger.error(f"File is empty: {file_path}.")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while loading data: {e}")
            raise
            
    def clean_data(self, df: pd.DataFrame, fit_scaler: bool = True) -> pd.DataFrame:
        """
        Clean the customer data by handling missing values and normalizing.
        """
        if df.empty:
            logger.error("Cannot clean an empty DataFrame.")
            raise ValueError("Input DataFrame is empty.")
            
        logger.info("Starting data cleaning process...")
        df_clean = df.copy()
        
        # Handle missing values using mean imputation
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            logger.info(f"Imputing missing values for numeric columns: {list(numeric_cols)}")
            df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].mean())
        
        logger.info("Filling remaining missing categorical values with 'Unknown'.")
        df_clean.fillna("Unknown", inplace=True)
        
        # Normalize numerical features
        if len(numeric_cols) > 0:
            logger.info("Scaling numerical features.")
            if fit_scaler:
                df_clean[numeric_cols] = self.scaler.fit_transform(df_clean[numeric_cols])
                self._is_fitted = True
            else:
                if not self._is_fitted:
                    logger.warning("Scaler has not been fitted, fitting now despite 'fit_scaler=False'.")
                    df_clean[numeric_cols] = self.scaler.fit_transform(df_clean[numeric_cols])
                    self._is_fitted = True
                else:
                    df_clean[numeric_cols] = self.scaler.transform(df_clean[numeric_cols])
        
        logger.info("Data cleaning completed.")
        return df_clean

    def prepare_data(self, file_path: Union[str, Path]) -> pd.DataFrame:
        """
        End-to-end load and clean.
        """
        try:
            df = self.load_data(file_path)
            return self.clean_data(df, fit_scaler=True)
        except Exception as e:
            logger.error(f"Failed to prepare data: {e}")
            raise

# Backward compatible function wrappers returning the same interface for safety,
# though ideally scripts would instantiate CustomerDataProcessor directly.
_processor = CustomerDataProcessor()

def load_data(file_path: Union[str, Path]) -> pd.DataFrame:
    return _processor.load_data(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    return _processor.clean_data(df, fit_scaler=True)

def prepare_data(file_path: Union[str, Path]) -> pd.DataFrame:
    return _processor.prepare_data(file_path)