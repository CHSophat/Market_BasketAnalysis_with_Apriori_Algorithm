
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        """Loads data from the csv file."""
        try:
            logger.info(f"Loading data from {self.filepath}")
            df = pd.read_csv(self.filepath)
            logger.info(f"Data loaded successfully. Shape: {df.shape}")
            return df
        except FileNotFoundError:
            logger.error(f"File not found at {self.filepath}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
