import pytest
from application import app  # ajusta según tu nombre de app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Probar la ruta raíz '/'"""
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hello, World!" in res.data
