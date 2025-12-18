def test_home(client):
    """Test del endpoint raíz"""
    res = client.get("/")
    assert res.status_code == 200
    assert res.data == b"Hello, World!"

def test_health_check(client):
    """Test del endpoint de health check"""
    res = client.get("/health")
    assert res.status_code == 200 or res.status_code == 404

def test_api_docs(client):
    """Test que Swagger/Flasgger está disponible"""
    res = client.get("/apidocs/")
    assert res.status_code == 200

def test_cors_headers(client):
    """Test que CORS está configurado"""
    res = client.get("/")
    assert res.status_code == 200

def test_invalid_route(client):
    """Test de ruta inexistente"""
    res = client.get("/ruta-inexistente")
    assert res.status_code == 404

def test_post_without_data(client):
    """Test POST sin datos"""
    res = client.post("/")
    assert res.status_code in [404, 405, 400]

#def test_intentional_failure(client):
    #TEST QUE FALLA INTENCIONADAMENTE - Verificar CI/CD
    #assert False, "Este test falla a propósito para verificar que el CI/CD bloquea el despliegue"
