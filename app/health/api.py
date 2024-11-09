from flask import Blueprint, current_app, jsonify

from app.health.service import Health


health_bp = Blueprint("health", __name__)


@health_bp.route("/healthz", methods=["GET"])
def healthz():
    response = Health.status()
    current_app.logger.info(f"healthz endpoint requested.: {response}")
    return jsonify(response), 200
