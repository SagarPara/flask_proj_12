import requests
import pytest
from main import app

# proxy to a live server
@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get("/")
    print(resp)
    assert resp.status_code == 200
    #assert resp.text == "<h2>Loan Application</h2>"



def test_predict(client):
    test_data =  { 
        "Gender":0.0,
        "Married":0.0,
        "ApplicationIncome":0,
        "LoanAmount":0,
        "Credit_History":0
    
    
    
    }
    

    resp = client.post("/submit", json=test_data)
    assert resp.status_code == 200
    #assert resp.json == {"Loan Approved Status: Rejected"}
    
    #response = client.get("/submit")
    #print(response)
    #assert response.status_code == 200
    #prediction = resp.json()
    #print(prediction)
    
    #assert "prediction" in prediction #check if the respose contains a "prediction" key
