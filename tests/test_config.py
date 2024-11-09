from app.config import Config


def test_config_default_settings(monkeypatch):
    monkeypatch.delenv("HOST", raising=False)
    monkeypatch.delenv("PORT", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    monkeypatch.delenv("DEBUG", raising=False)

    # when
    Config.load()

    # then
    assert Config.host == "0.0.0.0"
    assert Config.port == 8080
    assert Config.log_level == "INFO"
    assert Config.debug is False


def test_config_custom_settings(monkeypatch):
    monkeypatch.setenv("HOST", "127.0.0.1")
    monkeypatch.setenv("PORT", "5000")
    monkeypatch.setenv("LOG_LEVEL", "ERROR")
    monkeypatch.setenv("DEBUG", "True")

    # when
    Config.load()

    # then
    assert Config.host == "127.0.0.1"
    assert Config.port == 5000
    assert Config.log_level == "ERROR"
    assert Config.debug is True
