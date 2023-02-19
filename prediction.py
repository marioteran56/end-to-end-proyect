import joblib
from combined_attributes_adder import CombinedAttributesAdder

def predict(data, model_name):
    model = joblib.load(f'models/{model_name}')
    pipeline = joblib.load('models/pipeline.sav')
    transformed_data = pipeline.transform(data)
    return model.predict(transformed_data)