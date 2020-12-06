from math import sqrt, floor
from flask import render_template, make_response, request
from flask_restful import Resource
from Forms import PrimesForm


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
        prime_numbers_arr = []
        while current_number <= input_b:
            test_result = self.if_prime(current_number)
            if test_result:
                prime_numbers_arr.append(current_number)
            current_number += 1
        return prime_numbers_arr

    def if_prime(self, number):

        found = False
        for i in range(2, floor(sqrt(number))+1):
            if divmod(number, i)[1] == 0:
                found = True
                break
        return not found



