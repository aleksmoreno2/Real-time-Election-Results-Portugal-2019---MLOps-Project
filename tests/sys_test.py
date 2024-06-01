from sklearn.ensemble import RandomForestRegressor
from fastapi import FastAPI
from pydantic import BaseModel
from src.stages.data_split import data_split
from src.stages.evaluate import data_split

app = FastAPI()

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

