
from mlxtend.frequent_patterns import association_rules
import logging

logger = logging.getLogger(__name__)

class RulesGenerator:
    def __init__(self, metric="lift", min_threshold=1.0):
        self.metric = metric
        self.min_threshold = min_threshold

    def generate_rules(self, frequent_itemsets):
        """
        Generates association rules from frequent itemsets.
        """
        logger.info(f"Generating rules with metric='{self.metric}' and threshold={self.min_threshold}")
        try:
            rules = association_rules(frequent_itemsets, metric=self.metric, min_threshold=self.min_threshold)
            logger.info(f"Generated {len(rules)} rules.")
            return rules
        except Exception as e:
            logger.error(f"Error generating rules: {e}")
            raise
