from app.mpesa import mpesa_bp
from flask import jsonify

@mpesa_bp.app_errorhandler(404)
def not_founde(e):

    response = {"Message": "Resource Endpoint Not Found"}

    return jsonify(response), 404


@mpesa_bp.app_errorhandler(500)
def internal_error(e):

    response = {"Message": "Oups! Something Went Wrong"}

    return jsonify(response), 500