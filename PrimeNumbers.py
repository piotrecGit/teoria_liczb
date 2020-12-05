from math import sqrt, floor

from flask import render_template, make_response, request
from flask_restful import Resource
from Forms import EuklidesForm, PrimesForm


class PrimeNumbers(Resource):

    def get(self):
        myForm = PrimesForm()
        return make_response(render_template("prime_numbers.html", form=myForm))


    def post(self):
        myForm = PrimesForm(request.form)
        errors_string = ""
        if myForm.validate():
            a = int(request.form['od'])
            b = int(request.form['do'])
            exchange = False
            if b<a:
                a, b = b, a
                exchange = True

            result = self.prime_numbers(a, b)
            return make_response(render_template("prime_numbers.html", form=myForm, data=result, exchange=exchange))
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            return make_response(render_template("prime_numbers.html", form=myForm, occured_errors = errors_string))

    def prime_numbers(self, input_a, input_b):
        current_number = input_a
        prime_numbers = []
        while current_number <= input_b:
            test_result = self.if_prime(current_number)
            if test_result:
                prime_numbers.append(current_number)
            current_number += 1
        print(prime_numbers)

        #     an_item = dict(counter=counter, a=a, b=b, pa=pa, old_pa=old_pa, qa=qa, old_qa=old_qa, pb=pb, qb=qb)
        #     items.append(an_item)
        #
        #     wielokrotnosc = divmod(a, b)[0]
        #     reszta = divmod(a, b)[1]
        #     old_pa = pa
        #     old_qa = qa
        #     a = b
        #     b = reszta
        #     pa = pb
        #     qa = qb
        #     pb = old_pa - wielokrotnosc * pb
        #     qb = old_qa - wielokrotnosc * qb
        #
        # an_item = dict(counter="Na wyjściu", a=a, b=b, pa=pa, old_pa=old_pa, qa=qa, old_qa=old_qa, pb=pb, qb=qb)
        # items.append(an_item)

        return prime_numbers

    def if_prime(self, number):

        prime = True
        for i in range(2, floor(sqrt(number))):
            if divmod(number, i)[1] == 0:
                prime = False
                break

        return prime



