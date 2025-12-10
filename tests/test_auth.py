import pytest
import json

def test_register_user(client):
    """Test de registro de usuario"""
    payload = {
        "username": "testuser",
        "password": "testpass123",
        "nombre": "Test",
        "apellidos": "User",
        "email": "test@example.com",
        "telefono": "123456789"
    }
    res = client.post('/register', 
                      data=json.dumps(payload),
                      content_type='application/json')
    assert res.status_code in [200, 201, 409]  # 409 si ya existe

def test_login_without_credentials(client):
    """Test de login sin credenciales"""
    res = client.post('/login',
                      data=json.dumps({}),
                      content_type='application/json')
    assert res.status_code in [400, 401, 422]

def test_login_invalid_credentials(client):
    """Test de login con credenciales inválidas"""
    payload = {
        "username": "usernoexiste",
        "password": "wrongpass"
    }
    res = client.post('/login',
                      data=json.dumps(payload),
                      content_type='application/json')
    assert res.status_code in [401, 404]
