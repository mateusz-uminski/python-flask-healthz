import pytest
from app import app


def test_flask_app_is_created():
    # when
    flask_app = app.create()

    # then
    assert flask_app is not None


@pytest.fixture
def client():
    flask_app = app.create()
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client
