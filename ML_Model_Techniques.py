from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class ModelTrainer:
    def __init__(self, data):
        self.data = data

    def train_model(self):
        X = self.data[['temperature', 'humidity']]
        y = self.data['rainfall']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        return model

# Usage:
trainer = ModelTrainer(preprocessed_data)
model = trainer.train_model()
