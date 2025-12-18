import pytest
import os
import mongomock
import bcrypt
from application import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'test-secret-key'
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_mongo(monkeypatch):
    """Mock de MongoDB usando mongomock"""
    mock_client = mongomock.MongoClient()
    
    # Reemplazar el cliente real por el mock
    import application
    monkeypatch.setattr(application, 'myclient', mock_client)
    
    # Crear datos de prueba
    mydb = mock_client["Clinica"]
    
    # Crear contraseña hasheada con bcrypt
    hashed_password = bcrypt.hashpw('password123'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Crear colección de usuarios con datos de ejemplo
    usuarios_col = mydb["usuarios"]
    usuarios_col.insert_one({
        "username": "testuser",
        "password": hashed_password,
        "name": "Test",
        "lastname": "User",
        "email": "test@test.com",
        "phone": "123456789",
        "date": "01/01/2000"
    })
    
    # Crear colección de centros con datos de ejemplo
    centros_col = mydb["centros"]
    centros_col.insert_one({
        "nombre": "Centro Test",
        "direccion": "Calle Test 123",
        "telefono": "987654321"
    })
    
    return mock_client

@pytest.fixture
def app_context():
    """Fixture para contexto de aplicación"""
    with app.app_context():
        yield app
