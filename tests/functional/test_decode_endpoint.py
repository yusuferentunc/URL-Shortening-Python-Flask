def test_decode_post_url(app):
    """Test decode endpoint's normal behaviour"""
    response = app.post("/decode",  json={"short_url": "http://short.est/example"})
    assert response.status_code == 200
    assert response.json.get('result') is None


def test_decode_get_method(app):
    """Test decode endpoint with not allowed method"""
    response = app.get("/decode")
    assert response.status_code == 405


def test_decode_malformed_url(app):
    """Test decode endpoint with mistype/malformed url"""
    response = app.post("/decode", json={"short_url": "example.org/malformed"})
    assert response.status_code == 400
    assert response.json.get('error') == '400 Bad Request: Invalid URL'


def test_decode_empty_json(app):
    """Test decode endpoint with empty json input"""
    response = app.post("/decode", json={})
    assert response.status_code == 400
    assert response.json.get('error') == "400 Bad Request: Invalid URL"


def test_decode_without_json(app):
    """Test decode endpoint without json input"""
    response = app.post("/decode", data='unrelated data')
    assert response.status_code == 400

