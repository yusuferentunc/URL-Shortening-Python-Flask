import pytest
from main import create_app


@pytest.fixture
def app():
    """Create url shortening service's a test client fixture for functional testing"""
    app = create_app()
    app.debug = True
    return app.test_client()


# curl localhost:5000/post