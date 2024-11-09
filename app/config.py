import os
import sys
import logging


class Config:
    host = "0.0.0.0"
    port = 5000
    log_level = "INFO"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    debug = False

    @classmethod
    def load(cls):
        cls.host = os.getenv("HOST", "0.0.0.0")
        cls.port = int(os.getenv("PORT", 8080))
        cls.log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        cls.debug = bool(os.getenv("DEBUG", False))

    @classmethod
    def configure_logger(cls, app):
        app.logger.setLevel(cls.log_level)

        app.logger.handlers.clear()
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(cls.log_level)
        stream_handler.setFormatter(logging.Formatter(cls.log_format))
        app.logger.addHandler(stream_handler)

        werkzeug_logger = logging.getLogger('werkzeug')
        werkzeug_logger.setLevel(logging.ERROR)

        app.logger.info(f"Log level: {cls.log_level}")
