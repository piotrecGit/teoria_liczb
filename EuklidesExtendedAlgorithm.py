from flask import render_template, make_response, request
from flask_restful import Resource
from flask_wtf import FlaskForm, form
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from Forms import EuklidesForm


class EuklidesExtendedAlgorithm(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        myForm = EuklidesForm()
        return make_response(render_template("euklides_extended_algorithm.html", form=myForm))

# Rozszerzony  algorytm  Euklidesa
# wynikiem sa trzy liczby :  [ r ,  p ,  q ]
# takie, ze: NWD(a, b) = r = p*a + q*b

    def post(self):
        a = int(request.form['a'])
        b = int(request.form['b'])
        result = self.rozszerzony_euklides(a, b)
        headers = {'Content-Type': 'text/html'}
        myForm = EuklidesForm()
        return make_response(render_template("euklides_extended_algorithm.html", form=myForm))

    def rozszerzony_euklides(self, a, b):

        assert a != 0, "Liczba a nie może być zerem."
        assert b != 0, "Liczba b nie może być zerem."
        old_b = b
        pa = 1
        qa = 0
        pb = 0
        qb = 1

        while b != 0:
            # print(old_a.__str__() + " = " + q.__str__() + " * " + a.__str__() + " + " + r.__str__())
            # print(r.__str__() + " = " + old_a.__str__() + " - " + q.__str__() + " * " + a.__str__())
            # print(r.__str__() + " = " + old_a.__str__() + " - " + q.__str__()  + " * (" + old_a.__str__() + " - " + q.__str__() + " * " + a.__str__() + ")")
            # print("------------------------------------------------")
            # dzielenie bez reszty : "ile razy a sie miesci w b"
            wielokrotnosc = divmod(a, b)[0]
            reszta = divmod(a, b)[1]
            old_pa = pa
            old_qa = qa
            a = b
            b = reszta
            pa = pb
            qa = qb
            pb = old_pa - wielokrotnosc * pb
            qb = old_qa - wielokrotnosc * qb

        return  [a, pa if pa >= 0 else pa + old_b, qa]





