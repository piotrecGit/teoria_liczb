
import time
import random

from flask import render_template, make_response, request
from flask_restful import Resource
from Forms import FermatTestForm


class FermatTest(Resource):

    def get(self):

        myForm = FermatTestForm()
        return make_response(render_template("fermat_test.html", form=myForm))

    def post(self):

        myForm = FermatTestForm(request.form)
        errors_string = ""

        if myForm.validate():
            liczba = int(request.form['liczba'])
            dokladnosc = int(request.form['dokladnosc'])
            start_time = time.time()
            fermat_result = self.fermat_prime_test(liczba, dokladnosc)
            computation_time = (time.time() - start_time)
            fermat_result += "<br>Czas wykonywania obliczeń wyniósł: " + computation_time.__str__() + " sekundy"
            return make_response(render_template("fermat_test.html", form=myForm, data = fermat_result))
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            return make_response(render_template("fermat_test.html", form=myForm, occured_errors=errors_string))

    def fermat_prime_test(self, p, k):
        result_string = ""
        for i in range(1, k+1):
            a = self.losowanie(p)
            test_result = pow(a, p - 1, p)
            result_string += ("<br><strong>Krok " + i.__str__() + ":</strong><br>" + "wylosowano a = " + a.__str__() + "<br>a^(p-1) mod p = " + a.__str__() +
                  "^" + (p-1).__str__() +" mod " + p.__str__() + " = " + test_result.__str__() + "<br>")
            if int(test_result) != 1:
                result_string = "Liczba p = <strong>" + p.__str__() + "</strong> nie jest pierwsza<br><br>" + result_string
                return result_string
                break
        result_string = "Liczba p = <strong>" + p.__str__() + "</strong> jest prawdopodobnie pierwsza<br><br>" + result_string
        return result_string

    def losowanie(self, liczba):
        randomized = random.randrange(2, liczba-1, 1)
        return randomized


