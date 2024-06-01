import requests
import pytest
from src.stages.data_split import data_split
from sklearn.ensemble import RandomForestRegressor

def test ():
    prediction = requests.post(
        "http://127.0.0.1:3000/predict",
        headers={"content-type": "application/json"},
        data='{"City": "Pune", "PaymentTier": 0, "Age": 0, "Gender": "Female", "EverBenched": "No", "ExperienceInCurrentDomain": 0}',
    ).text

    assert prediction[0] in ["0", "1"]

def test_data():
    X_train, X_test, y_train, y_test = data_split()
    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0
