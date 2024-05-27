class Predictor:
    def __init__(self, model):
        self.model = model

    def predict(self, sensor_data):
        # Perform prediction using the trained model
        return self.model.predict(sensor_data)

# Usage:
predictor = Predictor(model)
sensor_data = [[25.0, 60.0]]  # Example sensor data
prediction = predictor.predict(sensor_data)
print("Predicted Rainfall:", prediction)
