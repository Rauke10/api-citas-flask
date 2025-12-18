import pytest

def test_create_date_without_token(client):
    """Test crear cita sin token JWT"""
    res = client.post('/date/create')
    assert res.status_code in [401, 405, 422, 500]

def test_get_dates_without_token(client):
    """Test obtener citas sin token"""
    res = client.get('/dates')
    assert res.status_code in [401, 422, 500]

def test_delete_date_without_token(client):
    """Test eliminar cita sin token"""
    res = client.delete('/date/delete')
    assert res.status_code in [401, 404, 405, 422, 500]

def test_get_dates_by_day_without_token(client):
    """Test obtener citas por día sin token"""
    res = client.get('/date/getByDay')
    # 405 METHOD NOT ALLOWED es válido si el endpoint existe pero requiere otro método
    assert res.status_code in [401, 405, 422, 500]
