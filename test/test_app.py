from requests import Response
from fastapi.testclient import TestClient
from lard_to_philosophy.app import app

client = TestClient(app)


def test_hello():
    response: Response = client.get("/hello")
    assert response.status_code == 200
    assert response.text == '"Hello World"'
