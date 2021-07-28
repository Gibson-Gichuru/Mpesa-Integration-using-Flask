from flask import Flask


mpesa = Flask(__name__)

@mpesa.route('/')
def index():

    return "welcome to mpesa integration using flask"


if __name__ == "__main__":

    mpesa.run(debug = True)