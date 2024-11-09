from app.health.service import Health


def test_health_status():
    # when
    response = Health.status()

    # then
    assert response == {"status": "healthy"}
