
import  os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    ## Flask app configs


    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY')


    #Mpesa app configs

    MPESA_CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    MPESA_CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    MPESA_BUSINESS_CODE = os.environ.get('BUSINESS_CODE')
    MPESA_PASS_KEY = os.environ.get("PASSKEY")


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