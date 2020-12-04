import datetime

from flask import request, render_template, make_response
from flask_restful import Resource
from ApiResponse import ApiResponse
from Config import ProjectRequirements
from HashFunctions import HashFunctions

HashFunctions = HashFunctions()
project_requirements = ProjectRequirements()


class Home(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("home.html"))


