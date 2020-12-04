from flask_restful import Api

from HomeApi import Home
from Config import GeneralConfig
from FilesTransportApi import FilesTransportApi
from HashFunctions import HashFunctions
from AdditionalFunctions import AdditionalFunctions
from flask import Flask
from ExampleClass import ExampleClass

"""Start configuration"""
app = Flask(__name__)
app_config = GeneralConfig()
api = Api(app)

"""Helpers"""
HashFunctions = HashFunctions()
AdditionalFunctions = AdditionalFunctions()

"""Api methods"""
api.add_resource(Home, '/', endpoint='home')
api.add_resource(FilesTransportApi, '/file/download/<path:file_name>', endpoint='file_download')
api.add_resource(FilesTransportApi, '/file/upload', endpoint='file_upload')
api.add_resource(ExampleClass, '/samples', endpoint='samples_get')
api.add_resource(ExampleClass, '/sample/add', endpoint='sample_add')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
