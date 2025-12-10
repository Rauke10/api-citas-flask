import pytest

def test_get_centers_without_token(client):
    """Test obtener centros sin token JWT"""
    res = client.get('/centers')
    assert res.status_code in [401, 422]  # No autorizado

def test_get_centers_with_invalid_token(client):
    """Test obtener centros con token inválido"""
    headers = {'Authorization': 'Bearer token_invalido'}
    res = client.get('/centers', headers=headers)
    assert res.status_code in [401, 422]
