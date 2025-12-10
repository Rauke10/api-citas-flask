import pytest
from application import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def app_context():
    """Fixture para contexto de aplicación"""
    with app.app_context():
        yield app
