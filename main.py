
from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.apriori_model import AprioriModel
from src.rules_generator import RulesGenerator
import os

def main():
    print("Association Analysis Apriori Pipeline")
    
    # 1. Load Data
    data_path = os.path.join("data", "raw", "grocery_orders.csv")
    loader = DataLoader(data_path)
    try:
        df = loader.load_data()
    except Exception:
        print("Failed to load data. Exiting.")
        return

    # 2. Preprocess
    preprocessor = Preprocessor()
    processed_df = preprocessor.preprocess(df)
    
    # Note: processed_df currently needs to be in a specific format for Apriori
    # This is just a skeleton.
    
    # 3. Model
    # model = AprioriModel(min_support=0.01)
    # frequent_itemsets = model.find_frequent_itemsets(processed_df)
    
    # 4. Rules
    # generator = RulesGenerator()
    # rules = generator.generate_rules(frequent_itemsets)
    
    # 5. Save Results
    # frequent_itemsets.to_csv("results/frequent_itemsets.csv", index=False)
    # rules.to_csv("results/association_rules.csv", index=False)
    
    print("Done.")

if __name__ == "__main__":
    main()
