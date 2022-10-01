def test_encode_post_url(app):
    """Test encode endpoint's normal behaviour"""
    response = app.post("/encode",  json={"url": "https://example.org/example"})
    assert response.status_code == 200
    assert response.json.get('result')


def test_encode_get_method(app):
    """Test encode endpoint with not allowed method"""
    response = app.get("/encode")
    assert response.status_code == 405


def test_encode_malformed_url(app):
    """Test encode endpoint with mistype/malformed url"""
    response = app.post("/encode", json={"url": "example.org/malformed"})
    assert response.status_code == 400
    assert response.json.get('error') == '400 Bad Request: Invalid URL'


def test_encode_empty_json(app):
    """Test encode endpoint with empty json input"""
    response = app.post("/encode", json={})
    assert response.status_code == 400
    assert response.json.get('error') == "400 Bad Request: Invalid URL"


def test_encode_without_json(app):
    """Test encode endpoint without json input"""
    response = app.post("/encode", data='unrelated data')
    assert response.status_code == 400

