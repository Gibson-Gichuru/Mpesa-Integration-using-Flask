from flask.globals import current_app
from . import mpesa_bp

from app.mpesa_utils import access_token

@mpesa_bp.route('/')
def index():

    get_access_token = access_token(current_app.config['MPESA_APP_CONSUMER_KEY'],
                                    current_app.config['MPESA_APP_CONSUMER_SECRET'], current_app.config['MPESA_APP_AUTH_URL'])

    return "Welcome to Mpesa Integration To Flask"