from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Initialize App
app = FastAPI(title="ChurnGuard API", version="1.0.0", description="Predict Customer Churn Probability")

# Load Model
MODEL_PATH = "models/churn_model.joblib"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model not found at {MODEL_PATH}. Run 'python src/train.py' first.")

model = joblib.load(MODEL_PATH)

# Define Input Schema (Pydantic)
class CustomerData(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

    class Config:
        json_schema_extra = {
            "example": {
                "CreditScore": 600,
                "Geography": "France",
                "Gender": "Male",
                "Age": 40,
                "Tenure": 3,
                "Balance": 60000.0,
                "NumOfProducts": 2,
                "HasCrCard": 1,
                "IsActiveMember": 1,
                "EstimatedSalary": 50000.0
            }
        }

@app.get("/")
def home():
    return {"status": "healthy", "message": "ChurnGuard API is running"}

@app.post("/predict")
def predict(data: CustomerData):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data.dict()])
        
        # Predict
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]
        
        return {
            "churn_prediction": int(prediction),
            "churn_probability": float(round(probability, 4)),
            "risk_level": "High" if probability > 0.7 else "Medium" if probability > 0.3 else "Low"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
