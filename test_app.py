import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_calculation_with_grade(client):
    response = client.post('/calculate', json={"marks": [80, 90, 70]})
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['total'] == 240
    assert json_data['average'] == 80.0
    assert json_data['grade'] == 'B' # Test the new grade functionality
