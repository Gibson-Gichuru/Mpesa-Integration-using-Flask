# flask related imports
from flask import current_app

# Python Standard imports
import base64
from flask.app import Flask
from flask.wrappers import Response
import requests
from datetime import datetime
import json

import pdb


class Mpesa:

    def __init__(self):

        self.consumer_key = current_app.config['MPESA_CONSUMER_KEY']
        self.consumer_secret = current_app.config['MPESA_CONSUMER_SECRET']

        self.auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
        self.stk_push_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"


    def format_phone_number(self, number):

        formart_number = list(number)
        formart_number[0] = "254"

        return "".join(formart_number)

    def access_token(self):

        row_string = f"{self.consumer_key}:{self.consumer_secret}".encode('utf-8')

        encoded_string = base64.b64encode(row_string).decode('utf-8')

        headers = {"Authorization": f"Basic {encoded_string}"}

        query_string = {"grant_type": "client_credentials"}

        response_data = requests.get(
            self.auth_url, headers=headers, params=query_string)

        access_token = response_data.json()['access_token']

        return  access_token

    def lipa_na_mpesa_password(self):

        lipa_time = datetime.now().strftime("%Y%m%d%H%M%S")

        business_code = current_app.config['MPESA_BUSINESS_CODE']
        pass_key = current_app.config['MPESA_PASS_KEY']

        raw_transaction_password = business_code + pass_key + lipa_time

        transaction_password = base64.b64encode(
            raw_transaction_password.encode('utf8'))

        return transaction_password.decode('utf8'), lipa_time

    def push_lipa_na_mpesa_stk(self, number):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.access_token()}"
        }

        payload = {
            "BusinessShortCode": current_app.config['MPESA_BUSINESS_CODE'],
            "Password": self.lipa_na_mpesa_password()[0],
            "Timestamp": self.lipa_na_mpesa_password()[1],
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 1,
            "PartyA": self.format_phone_number(number),
            "PartyB": 174379,
            "PhoneNumber": self.format_phone_number(number),
            "CallBackURL": "https://mydomain.com/path",
            "AccountReference": "CompanyXLTD",
            "TransactionDesc": "Payment of X"
        }

        response = requests.post(
            self.stk_push_url, json = payload, headers=headers)

        if response.status_code == 200:

            return True

        else:

            False
