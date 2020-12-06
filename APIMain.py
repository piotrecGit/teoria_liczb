from AdditionalFunctions import AdditionalFunctions
from Config import GeneralConfig
from EuklidesExtendedAlgorithm import EuklidesExtendedAlgorithm
from EulerFunction import EulerFunction
from Factorization import Factorization
from FermatTest import FermatTest
from flask import Flask
from flask_restful import Api
from Home import Home
from PrimeNumbers import PrimeNumbers
from RSADecrypt import RSADecrypt
from RSAEncrypt import RSAEncrypt
from RSAKeysPairGenerate import RSAKeysPairGenerate


"""Start configuration"""
app = Flask(__name__)
app_config = GeneralConfig()
app.config["SECRET_KEY"] = app_config.secret_key

api = Api(app)
"""Helpers"""
AdditionalFunctions = AdditionalFunctions()

"""Api methods"""
api.add_resource(Home, '/', endpoint='home')
api.add_resource(PrimeNumbers, '/prime_numbers', endpoint='prime_numbers')
api.add_resource(FermatTest, '/fermat_test', endpoint='fermat_test')
api.add_resource(Factorization, '/factorization', endpoint='factorization')
api.add_resource(EulerFunction, '/euler_function', endpoint='euler_function')
api.add_resource(EuklidesExtendedAlgorithm, '/euklides_extended_algorithm', endpoint='euklides_extended_algorithm')
api.add_resource(RSAKeysPairGenerate, '/rsa_keys_pair_generate', endpoint='rsa_keys_pair_generate')
api.add_resource(RSAEncrypt, '/rsa_encrypt', endpoint='rsa_encrypt')
api.add_resource(RSADecrypt, '/rsa_decrypt', endpoint='rsa_decrypt')

if __name__ == "__main__":
    app.run(debug=app_config.debug_mode, host='0.0.0.0')
