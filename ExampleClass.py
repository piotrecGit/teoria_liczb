import datetime

from flask import request
from flask_restful import Resource
from sqlalchemy.sql.functions import count, min
from ApiResponse import ApiResponse
from Config import ProjectRequirements
from HashFunctions import HashFunctions

HashFunctions = HashFunctions()
project_requirements = ProjectRequirements()


class ExampleClass(Resource):
    def get(self, merchant_id, user_id, text_id):
            response_object = ApiResponse(404, 1, "Error, there is no samples for given data!", {})
            return response_object.response

    def post(self):
        response_object = ApiResponse(201, 0, "Success", {"sampleId": 1234, "sampleFile": "file.txt"})
        return response_object.response



