import pytest
from app import app


def test_healthz(client):
    # when
    response = client.get('/api/v1/healthz')

    # then
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


@pytest.fixture
def client():
    flask_app = app.create()
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client
