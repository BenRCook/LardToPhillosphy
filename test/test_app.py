from flask import Response


def test_hello(client):
    response: Response = client.get("/hello")
    assert response.status_code == 200
    assert response.data == b"Hello World"
