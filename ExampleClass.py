import datetime

from flask import request
from flask_restful import Resource
from ApiResponse import ApiResponse
from Config import ProjectRequirements
from HashFunctions import HashFunctions

HashFunctions = HashFunctions()
project_requirements = ProjectRequirements()


class ExampleClass(Resource):
    def get(self):
            response_object = ApiResponse(200, 0, "hello", {})
            return response_object.response

    def post(self):
        response_object = ApiResponse(201, 0, "Success", {"sampleId": 1234, "sampleFile": "file.txt"})
        return response_object.response



