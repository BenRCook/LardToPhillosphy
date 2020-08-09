import pytest
from lard_to_philosophy.app import app


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
