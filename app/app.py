from flask import Flask
from app.config import Config
from app.health.api import health_bp


def create():
    app = Flask(__name__)

    app.register_blueprint(health_bp, url_prefix='/api/v1')
    return app


if __name__ == '__main__':
    app = create()

    Config.load()
    Config.configure_logger(app)

    app.run(
        debug=Config.debug,
        host=Config.host,
        port=Config.port,
    )
