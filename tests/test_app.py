import pytest
import json
from app import create_app

@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    return app

@pytest.fixture
def client(app):
    return app.test_client()

class TestHealthEndpoint:
    def test_health_returns_200(self, client):
        response = client.get('/api/health')
        assert response.status_code == 200

    def test_health_returns_json(self, client):
        response = client.get('/api/health')
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'timestamp' in data
        assert 'version' in data

class TestInfoEndpoint:
    def test_info_returns_200(self, client):
        response = client.get('/api/info')
        assert response.status_code == 200

    def test_info_has_correct_fields(self, client):
        response = client.get('/api/info')
        data = json.loads(response.data)
        assert 'app' in data
        assert 'python_version' in data

class TestGreetEndpoint:
    def test_greet_valid_name(self, client):
        response = client.get('/api/greet/Neeharika')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'Neeharika' in data['message']

    def test_greet_invalid_name(self, client):
        response = client.get('/api/greet/123invalid')
        assert response.status_code == 400

class TestIndexPage:
    def test_index_loads(self, client):
        response = client.get('/')
        assert response.status_code == 200