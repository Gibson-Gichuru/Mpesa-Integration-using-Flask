from flask.globals import current_app
from flask import jsonify, url_for
from . import mpesa_bp

from app.mpesa_utils import Mpesa


@mpesa_bp.route('/')
def index():

    return "Welcome to Mpesa Integration To Flask"


@mpesa_bp.route('/sdk_push/<int:number>', methods=["GET", "POST"])
def sdk_push(number):

    mpesa = Mpesa()

    transact = mpesa.push_lipa_na_mpesa_stk(number)

    if transact:

        return jsonify({"message":"Please confirm your payment on your device"})

    else:

        return jsonify({"Message":"Transaction request failed"})
