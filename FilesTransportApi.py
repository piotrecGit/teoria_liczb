import os
import Config

from werkzeug.utils import secure_filename
from flask import send_from_directory, request
from flask_restful import Resource
from AdditionalFunctions import AdditionalFunctions
from ApiResponse import ApiResponse

files_config = Config.FilesSystemConfig()
AdditionalFunctions = AdditionalFunctions()


def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in files_config.allowed_extensions


class FilesTransportApi(Resource):

    def get(self, file_name):
        voices_directory = os.path.join(AdditionalFunctions.get_default_directory(), files_config.upload_folder)
        return send_from_directory(directory=voices_directory, filename=file_name)

    def put(self):
        voices_directory = os.path.join(AdditionalFunctions.get_default_directory(), files_config.upload_folder)
        # check if the post request has the file part
        if 'file' not in request.files:
            return ApiResponse(400, 1, "Error, no file part in the request", {})

        file = request.files['file']
        file_name = file.filename
        if file_name == '':
            return ApiResponse(400, 1, "No file selected for uploading", {})

        if file and allowed_file(file_name):
            file_name = secure_filename(file_name)

            file.save(os.path.join(voices_directory, file_name))
            response_object = ApiResponse(201, 0, "File successfully uploaded", {})
            return response_object.response
        else:
            response_object = ApiResponse(400, 1, "Allowed file types are: npy, png", {})
            return response_object.response


