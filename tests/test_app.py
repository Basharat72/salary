import pytest
from app.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Salary Predictor" in response.data

def test_prediction_post(client):
    response = client.post('/', data={'experience': '5'})
    assert response.status_code == 200
    assert b"Predicted Salary" in response.data
