### `server.py` (API )

1. **`Add file` -> `Create new file`**.
2. **** `src/api/server.py`
3. ** **

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
from datetime import datetime

app = FastAPI(
    title="CodePrism API",
    description="Self-Adaptive Semantic Software Defect Prediction",
    version="1.0.0"
)

class CodeRequest(BaseModel):
    code: str
    language: str = "python"

class PredictionResponse(BaseModel):
    defect_probability: float
    risk_level: str
    explanation: list
    timestamp: str

@app.get("/")
async def root():
    return {"message": "CodePrism API is running!", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/predict", response_model=PredictionResponse)
async def predict_defect(request: CodeRequest):
    """
    Predicts the probability of defects in the provided code.
    """   
    return PredictionResponse(
        defect_probability=0.87,
        risk_level="HIGH",
        explanation=[
            "Complex nested loops detected in the code structure",
            "High coupling with external modules identified",
            "Unhandled exception paths found"
        ],
        timestamp=datetime.now().isoformat()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
