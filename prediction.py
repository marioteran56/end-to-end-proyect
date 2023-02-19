import joblib

def predict(data, model_name):
    model = joblib.load(f'models/{model_name}')
    return model.predict(data)