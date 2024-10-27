import pytest
from starlette.testclient import TestClient

from ui.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_title(client):
    r = client.get("/")
    assert "<title>Fasthtml template: 0.0.1</title>" in r.text
