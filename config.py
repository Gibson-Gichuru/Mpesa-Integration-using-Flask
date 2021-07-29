
import  os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    ## Flask app configs

    SECRET_KEY = os.environ.get('SECRET_KEY')


    #Mpesa app configs

    MPESA_APP_CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    MPESA_APP_CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    MPESA_APP_AUTH_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate"


    ## Database Configs
    SQLALCHEMY_COMMITON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    @staticmethod
    def init_app(app):

        pass

class DevelopmentConfig(Config):

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):

    @staticmethod
    def init_app(app):
        
        pass



config = {'development': DevelopmentConfig, "production":ProductionConfig, 'default': DevelopmentConfig}