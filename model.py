from joblib import load
import pandas as pd
from preprocessing import preprocess_input,preprocess_input_churn



def predict_sales(input_data):
    # Load the trained model
    model = load('model/linear_regression_model.joblib')
    # Preprocess the input data
    processed_data = preprocess_input(input_data)
    # Make prediction
    prediction = model.predict(processed_data)
    return prediction[0]

def predict_churn_result(input_data):
    model = load('\model\customer_churn_model.joblib')
    # Preprocess the input data
    processed_data = preprocess_input_churn(input_data)
    # Make prediction
    prediction = model.predict(processed_data)
    return prediction[0]