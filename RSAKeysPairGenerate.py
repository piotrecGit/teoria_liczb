import random
import time

from flask import render_template, make_response, request
from flask_restful import Resource

from EuklidesExtendedAlgorithm import EuklidesExtendedAlgorithm
from EulerFunction import EulerFunction
from Forms import RSAKeysPairGenerateForm
from PrimeNumbers import PrimeNumbers


class RSAKeysPairGenerate(Resource):

    def get(self):
        myForm = RSAKeysPairGenerateForm()
        return make_response(render_template("rsa_keys_pair_generate.html", form=myForm))


    def post(self):
        myForm = RSAKeysPairGenerateForm(request.form)
        errors_string = ""
        euler = EulerFunction

        if myForm.validate():
            key_lenght = int(request.form['key_lenght'])
            number_p = 0
            number_q = 0
            miler_rabin_rounds = 1
            start_time = time.time()
            while not self.miller_rabin(number_p, miler_rabin_rounds): #prime.if_prime(self, number_p):
                number_p = self.losowanie_duzej_liczby(key_lenght)
            while number_q == 0 or number_p == number_q:
                while not self.miller_rabin(number_q, miler_rabin_rounds): #prime.if_prime(self, number_q):
                    number_q = self.losowanie_duzej_liczby(key_lenght)
            number_n = number_p * number_q
            result_string = "Wylosowana liczba pierwsza <strong>p</strong>:<br><br>" + number_p.__str__() + "<br><br>Wylosowana liczba pierwsza <strong>q</strong>:<br><br>" + number_q.__str__() + "<br><br>"

            result_string += "Liczba <strong>n = p * q (klucz publiczny - część n):</strong><br><br>" + (number_n).__str__() + "<br><br>"

            euler_p = euler.euler(self, number_p)[1]
            euler_q = euler.euler(self, number_q)[1]
            number_euler = euler_p * euler_q

            result_string += "Funkcja Eulera <strong>φ(n) = </strong><br><br>" + number_euler.__str__() + "<br><br>"

            number_e = 0
            euklides_result_inverse = 0
            euklides_result_nwd = 0

            prime = PrimeNumbers

            rands = prime.prime_numbers(self, 50000, 99999)

            while (euklides_result_inverse * number_e) % number_euler != 1:
                while euklides_result_nwd != 1:
                    while number_e >= number_n or number_e == 0 or number_e % 2 == 0 or number_e % 3 == 0 or number_e % 4 == 0 or number_e % 5 == 0 or number_e % 9 == 0:
                        number_e = rands[random.randrange(0, len(rands))]



                    euklides = EuklidesExtendedAlgorithm
                    euklides_result = euklides.rozszerzony_euklides(self, number_e, number_euler)['items'][-1]
                    euklides_result_nwd = euklides_result['a']
                    euklides_result_inverse = euklides_result['pa']


            number_inverse = euklides_result_inverse

            result_string += "Wylosowana liczba <strong>e (klucz publiczny - część e):</strong><br><br>" + number_e.__str__() + "<br><br>"
            result_string += "Odwrotność liczby <strong>e mod φ(n) (klucz prywatny):</strong><br><br>" + number_inverse.__str__() + "<br><br>"

            nwd_e_and_euler = 1


            computation_time = (time.time() - start_time)
            result_string += "<br>Czas wykonywania obliczeń wyniósł: " + round(computation_time, 6).__str__() + " sekundy"
            response = make_response(render_template("rsa_keys_pair_generate.html", form=myForm, data=result_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            response = make_response(render_template("rsa_keys_pair_generate.html", form=myForm, occured_errors=errors_string))
            response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
            response.headers['Cache-Control'] = 'public, max-age=0'
            return response

    def miller_rabin(self, n, k):

        # if n == 2 or n == 3:
        #     return True

        if n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0 or n % 9 == 0:
            return False


        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for i in range(1, k+1):
            a = random.randrange(1, n)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for j in range(1, r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def losowanie_duzej_liczby(self, bits):

        # in hex return '%X' % random.getrandbits(bits)
        number = -1
        while number < 0:
            number = random.getrandbits(bits)

        print(number)
        return  number