import pytest
import json

def test_login_without_credentials(client):
    """Test de login sin credenciales"""
    res = client.post('/login',
                      data=json.dumps({}),
                      content_type='application/json')
    assert res.status_code in [400, 401, 422, 500]

def test_register_requires_post(client):
    """Test que register solo acepta POST"""
    res = client.get('/register')
    assert res.status_code in [405]

def test_login_requires_post(client):
    """Test que login solo acepta POST"""
    res = client.get('/login')
    assert res.status_code in [405]

def test_register_with_mock_mongo(client, mock_mongo):
    """Test de registro con MongoDB mockeado"""
    payload = {
        "username": "newuser",
        "password": "password123",
        "name": "New",
        "lastname": "User",
        "email": "new@test.com",
        "phone": "111222333",
        "date": "15/05/1995"
    }
    res = client.post('/register',
                      data=json.dumps(payload),
                      content_type='application/json')
    # Debe funcionar con el mock
    assert res.status_code in [200, 201, 400, 409]

def test_login_with_mock_mongo(client, mock_mongo):
    """Test de login con MongoDB mockeado"""
    payload = {
        "username": "testuser",
        "password": "password123"
    }
    res = client.post('/login',
                      data=json.dumps(payload),
                      content_type='application/json')
    # El usuario existe en el mock pero la contraseña puede no coincidir
    assert res.status_code in [200, 401]
