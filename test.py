from app import app
import json

def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello Students!!!'

def test_data():
    response = app.test_client().get('/api/data')
    assert response.status_code == 200
    # Convert response.data from byte format to json
    data = json.loads(response.data)
    assert data == {"message": "Here's some JSON data", "status": "success"}
