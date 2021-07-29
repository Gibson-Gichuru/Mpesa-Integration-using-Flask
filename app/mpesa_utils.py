## flask related imports
from flask import current_app

## Python Standard imports
import base64
import requests

import json

def access_token(consumer_key, consumer_secret, auth_url):

    auth_token = base64.b64encode(f"{consumer_key}:{consumer_secret}".encode('utf8')).decode('utf8')

    headers = {"Authorization":f"Basic {auth_token}"}

    query_string = {"grant_type":"client_credentials"}

    response_data = requests.get(auth_url, headers = headers, params=query_string)

    return response_data