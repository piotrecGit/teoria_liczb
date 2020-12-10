import time

from flask import render_template, make_response, request
from flask_restful import Resource

from Forms import RSAEncryptForm


class RSAEncrypt(Resource):

    def get(self):
        myForm = RSAEncryptForm()
        return make_response(render_template("rsa_encrypt.html", form=myForm))

    def post(self):
        myForm = RSAEncryptForm(request.form)
        errors_string = ""

        if myForm.validate():
            M_string = request.form['M']
            M_bytes = bytes(M_string, "utf-8")
            M = int.from_bytes(M_bytes, byteorder="little", signed=False)
            e = int(request.form['e'])
            n = int(request.form['n'])
            start_time = time.time()
            result = pow(M, e, n)
            result_string = "Dla wiadomości <strong>M</strong>:<br><br>" + M.__str__() +\
                            "<br><br>słownie: (" + M_string + ")<br><br>zaszyfrowanej kluczem publicznym <strong>k(e, n)</strong>:<br><br>" + \
                             "<strong>e=</strong><br>" + e.__str__() + "<br><br><strong>n</strong>=<br>" + n.__str__() + \
                            "<br><br>szyfrogram <strong>C =</strong><br>" + result.__str__() + "<br><br>"

            computation_time = (time.time() - start_time)
            result_string += "<br>Czas wykonywania obliczeń wyniósł: " + round(computation_time, 6).__str__() + " sekundy"
            response = make_response(render_template("rsa_encrypt.html", form=myForm, data=result_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            response = make_response(render_template("rsa_encrypt.html", form=myForm, occured_errors=errors_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response
