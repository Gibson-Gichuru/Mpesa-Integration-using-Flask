from flask.globals import current_app
from flask import jsonify, url_for
from requests.api import request
from . import mpesa_bp

from app import db

from app.models import MpesaPayment

from app.mpesa_utils import Mpesa


@mpesa_bp.route('/')
def index():

    return "Welcome to Mpesa Integration To Flask"


@mpesa_bp.route('/sdk_push/<number>', methods=["GET", "POST"])
def sdk_push(number):

    mpesa = Mpesa()

    transact = mpesa.push_lipa_na_mpesa_stk(number)

    if transact:

        return jsonify({"message": "Please confirm your payment on your device"})

    else:

        return jsonify({"Message": "Transaction request failed"})


@mpesa_bp.route('/registerUrl')
def register_url():

    mpesa = Mpesa()

    headers = {"Authorization": f"Bearer {mpesa.access_token()}"}

    options = {"ShortCode": current_app.config['MPESA_BUSINESS_CODE'], "ConfirmationURL": url_for(
        'mpesa_bp.confirmation', _external=True), "ValidationURL": url_for('mpesa_bp.validation', _external=True)}


    return "register c2b urls"


@mpesa_bp.route('/validation')
def validation():

    context = {"ResultCode": 0, "ResultDesc":"Accepted"}

    return jsonify(context)

@mpesa_bp.route('/confirmation')
def confirmation():

    mpesa_body =request.body.decode('utf8')
    mpesa_payment = json.loads(mpesa_body)

    payment = MpesaPayment(

        first_name = mpesa_payment['firstName'],
        middle_name = mpesa_payment['middleName'],
        last_name = mpesa_payment['lastName'],
        description = mpesa_payment['TransID'],
        phone_number = mpesa_payment['MSISDN'],
        amount = mpesa_payment['TransAmount'],
        reference = mpesa_payment['BillRefNumber'],
        organization_balance= mpesa_payment['OrgAccountBalance'],
        type = mpesa_payment['TransactionType'],

    )

    db.session.add(payment)
    db.session.commit()

    
    context = {"ResultCode": 0, "ResultDesc":"Accepted"}

    return jsonify(context)