import time

from flask import render_template, make_response, request
from flask_restful import Resource

from Forms import RSADecryptForm


class RSADecrypt(Resource):

    def get(self):
        myForm = RSADecryptForm()
        return make_response(render_template("rsa_decrypt.html", form=myForm))

    def post(self):
        myForm = RSADecryptForm(request.form)
        errors_string = ""

        if myForm.validate():

            C = int(request.form['C'])
            d = int(request.form['d'])
            n = int(request.form['n'])
            start_time = time.time()
            result = pow(C, d, n)
            M_bytes = result.to_bytes(length=result.__sizeof__(), byteorder="little", signed=False)
            M = ""

            try:
                M = M_bytes.decode("utf-8")

            except:

                response = make_response(render_template("rsa_decrypt.html", form=myForm, occured_errors="Odszyfrowywanie nie powiodło się. Użyto nieprawidłowego szyfrogramu, klucza prywatnego lub modułu."))
                response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
                response.headers['Cache-Control'] = 'public, max-age=0'
                return response

            result_string = "Dla szyfrogramu <strong>C</strong>:<br><br>" + C.__str__() +\
                            "<br><br>odszyfrowanego kluczem prywatnym <strong>k(d, n)</strong>:<br><br>" + \
                             "<strong>d=</strong><br>" + d.__str__() + "<br><br><strong>n</strong>=<br>" + n.__str__() + \
                            "<br><br>wiadomość <strong>M =</strong><br>" + M.__str__() + "<br><br>"

            computation_time = (time.time() - start_time)
            result_string += "<br>Czas wykonywania obliczeń wyniósł: " + round(computation_time, 6).__str__() + " sekundy"
            response = make_response(render_template("rsa_decrypt.html", form=myForm, data=result_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            response = make_response(render_template("rsa_decrypt.html", form=myForm, occured_errors=errors_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response
