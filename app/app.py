
#import necessary libraries
import pandas as pd
import numpy as np
from fastapi import FastAPI
import pickle
import logging
import json
from requests import Request

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set the minimum logging level
handler = logging.StreamHandler()  # Send logs to console
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



# Model and transformer paths

# For local deployment
transformer_path = "models/preprocess_tranformer.pkl"
model_path = "models/lr_model.pkl"

# For Docker based deployments
# transformer_path = "app/models/preprocess_tranformer.pkl"
# model_path = "app/models/lr_model.pkl"


# load models
preprocess_transformer = pickle.load(open(transformer_path, "rb"))
model = pickle.load(open(model_path, "rb"))

def prep_data(data):
    """
    Preprocess the input data using the loaded transformer.
    """
    if isinstance(data, pd.DataFrame):  # Check if data is already a DataFrame
        pass
    else:                               # Convert data to DataFrame if it's not already
        data = pd.DataFrame(data)
    logger.info(f"Data reached prep_data function")  # Log the input data
    return preprocess_transformer.transform(pd.DataFrame(data))
    
def predict(data):
    """
    Predict using the loaded model.
    """
    # Preprocess the data
    data = prep_data(data)
    logger.info(f"Data after preprocessing in predict function")  # Log the preprocessed data
    # Make predictions
    prediction_probabilities = model.predict_proba(data)[:, 1]  # Get probabilities for the positive class
    # Convert to binary predictions
    predictions = [ 1 if prob >= 0.3 else 0 for prob in prediction_probabilities ]
    return predictions

# Create FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    logger.info("Root endpoint accessed")  # Log the access to the root endpoint
    return {
            "Project Name": "Bank Marketing Campaign Prediction"
            , "Description": "Predict whether a customer will subscribe to a term deposit based on bank marketing data."
            , "API Health": "Ok"
        }

@app.get("/predict")
def make_prediction(data: str):
    """
    Endpoint to make predictions based on input data.
    """
    # predictions = predict(data)
    # return {"predictions": predictions}
    data = eval(data)  # Convert string representation of list/dict to actual list/dict
    logging.info(f"Received data for prediction")
    try:
        # Make prediction
        logger.info(f"Received data for prediction in try block")  # Log the input data
        predictions = predict(data)
        logger.info(f"Predictions made")  # Log the predictions
        return {"predictions": predictions}  #pd.DataFrame(predictions, columns=["predictions"]).to_dict(orient='list')
    except Exception as e:
        return {"error": str(e)}


