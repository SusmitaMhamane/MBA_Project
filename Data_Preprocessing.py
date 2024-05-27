
import pandas as pd

class DataPreprocessor:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def preprocess_data(self):
        df = pd.read_sql_query("SELECT * FROM sensor_data", self.conn)
        # Perform preprocessing steps (e.g., handle missing values, normalize data, feature engineering)
        return df

# Usage:
preprocessor = DataPreprocessor('sensor_data.db')
preprocessed_data = preprocessor.preprocess_data()
