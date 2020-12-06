import time
from math import floor, sqrt

from flask import render_template, make_response, request
from flask_restful import Resource

from Factorization import Factorization
from Forms import EulerFunctionForm
from PrimeNumbers import PrimeNumbers


class EulerFunction(Resource):

    def get(self):
        myForm = EulerFunctionForm()
        return make_response(render_template("euler_function.html", form=myForm))


    def post(self):
        myForm = EulerFunctionForm(request.form)
        errors_string = ""
        result_string = "φ(n) = "
        result_dict = {}
        result_value = 1

        if myForm.validate():
            liczba = int(request.form['liczba'])
            prime = PrimeNumbers

            if not prime.if_prime(self, liczba):
                factors = Factorization()
                start_time = time.time()
                result = factors.factorization(liczba)
                computation_time = (time.time() - start_time)

                for i in result:
                    if i.__str__() in result_dict:
                        result_dict[i.__str__()] += 1
                    else:
                        result_dict[i.__str__()] = 1

                for i in result_dict:
                    result_value *= (int(i)-1) * pow(int(i), result_dict[i]-1)
                    result_string += ("(" + i + "-1) * " + i + "<sup>" + result_dict[i].__str__() + "-1</sup> * ")

                result_string = result_string.rstrip(' * ') + " = " + result_value.__str__()
                result_string += "<br>Czas wykonywania obliczeń wyniósł: " + round(computation_time, 6).__str__() + " sekundy"
            else:
                result_string = "Liczba n=<strong>" + liczba.__str__() + "</strong> jest pierwsza dlatego wartość funkcji Eulera wynosi dla niej φ(n) = n-1 = " + liczba.__str__() + "-1 = " + (liczba - 1).__str__()

            response = make_response(render_template("euler_function.html", form=myForm, data=result_string, liczba=liczba))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            response = make_response(render_template("euler_function.html", form=myForm, occured_errors=errors_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response

