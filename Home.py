from flask import render_template, make_response
from flask_restful import Resource


class Home(Resource):

    def get(self):
        response = make_response(render_template("home.html"))
        response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        response.headers['Cache-Control'] = 'public, max-age=0'
        return response


