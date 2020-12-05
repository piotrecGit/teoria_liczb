from flask import render_template, make_response, request
from flask_restful import Resource
from flask_restful import reqparse
from flask_wtf import FlaskForm, form
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from Forms import EuklidesForm



class EuklidesExtendedAlgorithm(Resource):

    def get(self):
        myForm = EuklidesForm()
        return make_response(render_template("euklides_extended_algorithm.html", form=myForm))

# Rozszerzony  algorytm  Euklidesa
# wynikiem sa trzy liczby :  [ r ,  p ,  q ]
# takie, ze: NWD(a, b) = r = p*a + q*b

    def post(self):
        myForm = EuklidesForm(request.form)
        errors_string = ""
        if myForm.validate():

            a = int(request.form['a'])
            b = int(request.form['b'])
            result = self.rozszerzony_euklides(a, b)
            return make_response(render_template("euklides_extended_algorithm.html", form=myForm, data=result))
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            return make_response(render_template("euklides_extended_algorithm.html", form=myForm, occured_errors = errors_string))

    def rozszerzony_euklides(self, input_a, input_b):
        a = input_a
        b = input_b
        # assert a != 0, "Liczba a nie może być zerem."
        assert b != 0, "Liczba b nie może być zerem."
        pa = 1
        qa = 0
        pb = 0
        qb = 1
        old_pa = 0
        old_qa = 0
        items = []
        counter = 0
        while b != 0:
            counter += 1
            an_item = dict(counter=counter, a=a, b=b, pa=pa, old_pa=old_pa, qa=qa, old_qa=old_qa, pb=pb, qb=qb)
            items.append(an_item)

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

        an_item = dict(counter="Na wyjściu", a=a, b=b, pa=pa, old_pa=old_pa, qa=qa, old_qa=old_qa, pb=pb, qb=qb)
        items.append(an_item)

        return {
                "items":items,
                "a": abs(a),
                "sign": pa,
                "pa": pa if pa >= 0 else pa + input_b,
                "qa": qa,
                "input_a": input_a,
                "input_b": input_b
        }





