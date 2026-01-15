
from mlxtend.frequent_patterns import apriori
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class AprioriModel:
    def __init__(self, min_support=0.01):
        self.min_support = min_support

    def find_frequent_itemsets(self, transactions_df):
        """
        Generates frequent itemsets using the Apriori algorithm.
        transactions_df: One-hot encoded DataFrame or suitable format for mlxtend apriori.
        """
        logger.info(f"Generating frequent itemsets with min_support={self.min_support}")
        # Note: input df must be bool/int (0/1) for apriori
        try:
            frequent_itemsets = apriori(transactions_df, min_support=self.min_support, use_colnames=True)
            logger.info(f"Found {len(frequent_itemsets)} frequent itemsets.")
            return frequent_itemsets
        except Exception as e:
            logger.error(f"Error in Apriori: {e}")
            raise
