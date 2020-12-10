import time

from flask import render_template, make_response, request
from flask_restful import Resource
from Forms import EuklidesForm



class EuklidesExtendedAlgorithm(Resource):

    def get(self):
        myForm = EuklidesForm()
        response=make_response(render_template("euklides_extended_algorithm.html", form=myForm))
        response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        response.headers['Cache-Control'] = 'public, max-age=0'

        return response

# Rozszerzony  algorytm  Euklidesa
# wynikiem sa trzy liczby :  [ r ,  p ,  q ]
# takie, ze: NWD(a, b) = r = p*a + q*b

    def post(self):
        myForm = EuklidesForm(request.form)
        errors_string = ""
        if myForm.validate():

            a = int(request.form['a'])
            b = int(request.form['b'])

            start_time = time.time()
            result = self.rozszerzony_euklides(a, b)
            computation_time = (time.time() - start_time)
            response = make_response(render_template("euklides_extended_algorithm.html", form=myForm, data=result, computation_time=round(computation_time, 6)))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response

        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            response = make_response(render_template("euklides_extended_algorithm.html", form=myForm, occured_errors = errors_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response

    def rozszerzony_euklides(self, input_a, input_b):
        a = int(input_a)
        b = int(input_b)
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
        if an_item['pa'] < 0:
            an_item['pa'] = an_item['pa'] + input_b
            pa = pa + input_b
        return {
                "items":items,
                "a": abs(a),
                "sign": pa,
                "pa": pa,
                "qa": qa,
                "input_a": input_a,
                "input_b": input_b
        }





