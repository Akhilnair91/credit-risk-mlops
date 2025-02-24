import os
import joblib
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# ✅ Construct the correct model path
model_path = os.path.join(os.path.dirname(__file__), "../models/xgboost.pkl")

# ✅ Load trained model
model = joblib.load(model_path)
print("✅ Model loaded successfully!")

@app.get("/")
def home():
    return {"message": "Welcome to the Credit Risk Prediction API! Use /predict/ for predictions."}

class CreditData(BaseModel):
    LIMIT_BAL: float
    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float
    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float

@app.post("/predict/")
def predict(data: CreditData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
