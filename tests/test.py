def test_create_cita(client):
    data = {"nombre": "Juan", "fecha": "2025-01-01"}
    res = client.post("/citas", json=data)
    assert res.status_code == 201

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200

def test_get_citas(client):
    res = client.get("/citas")
    assert res.status_code == 200

def test_get_cita_by_id(client):
    res = client.get("/citas/1")
    assert res.status_code == 200

def test_update_cita(client):
    data = {"nombre": "Pedro", "fecha": "2025-02-01"}
    res = client.put("/citas/1", json=data)
    assert res.status_code == 200