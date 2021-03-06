import time
from flask import render_template, make_response, request
from flask_restful import Resource
from Forms import FactorizationForm
from PrimeNumbers import PrimeNumbers
from sympy.ntheory import factorint


class Factorization(Resource):

    def get(self):
        myForm = FactorizationForm()
        response = make_response(render_template("factorization.html", form=myForm))
        response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        response.headers['Cache-Control'] = 'public, max-age=0'
        return response

    def post(self):
        myForm = FactorizationForm(request.form)
        errors_string = ""
        result_string = ""
        if myForm.validate():
            liczba = int(request.form['liczba'])
            prime = PrimeNumbers
            start_time = time.time()
            result = self.factorization(liczba)
            computation_time = (time.time() - start_time)
            if result[0] != liczba:

                if len(result) > 1:
                    result_string = liczba.__str__() + " = "
                    for i in result:
                        result_string += (str(i) + "*")
                    result_string = result_string.rstrip('*')
                    result_string += "<br>Czas wykonywania obliczeń wyniósł: " + round(computation_time, 6).__str__() + " sekundy"
            else:
                result_string = "Liczby <strong>" + liczba.__str__() + "</strong> nie da się rozłożyć na czynniki pierwsze ponieważ jest to liczba pierwsza."

            return make_response(render_template("factorization.html", form=myForm, data=result_string, liczba=liczba))
        else:
            print(myForm.errors)
            for key in myForm.errors:
                for value in myForm.errors[key]:
                    errors_string += "<li>" + key + ":  " + value + "</li>"

            return make_response(render_template("factorization.html", form=myForm, occured_errors = errors_string))


    def factorization(self, n):

        factors_dict = factorint(n)
        factors = []
        for i in factors_dict:
            for j in range(1, factors_dict[i] + 1):
                factors.append(i)
        return factors




    # def factorization(self, n):1
    #     array_of_factors = []
    #     while n > 1:
    #         for i in range(2, int(n) + 1):
    #             if n % i == 0:
    #                 n /= i
    #                 array_of_factors.append(i)
    #                 break
    #     return array_of_factors

    # def fermat(self, p, factors):
    #     p = int(p)
    #     x = ceil(sqrt(p))
    #
    #     while True:
    #         z = int((x * x) - p)
    #         y = floor(sqrt(z))
    #
    #         if z == (y * y):
    #             m = x + y
    #             n = x - y
    #             print(x, y, z, m, n, p)
    #             if n == 1:
    #                 print("break1 n=1")
    #                 break
    #
    #             self.fermat(m, factors)
    #             self.fermat(n, factors)
    #             return
    #         x += 1
    #         if (x + y) < p:
    #             print("break2 x:" + x.__str__() + " y: " + y.__str__() + " p: " + p.__str__())
    #
    #     factors.append(p)
    
    # def factorization_fermat(self, p):
    #
    #     p = int(p)
    #     factors = []
    #     while (p % 2) == 0:
    #         p /= 2
    #         factors.append(2)
    #     if p > 1:
    #         self.fermat(p, factors)
    #     return factors

    # def factorization_naive(self, input_a):
    #     current_number = input_a
    #     factors = []
    #     prime = PrimeNumbers()
    #     while current_number > 1:
    #         # print("current: " + current_number.__str__())
    #         prime_nums = prime.prime_numbers(2, floor(current_number/2))
    #         for i in prime_nums:
    #             # print(current_number.__str__() + " / " + str(i))
    #             if i >= floor(current_number/2):
    #                 i = current_number
    #             multiple = divmod(current_number, i)[0]
    #             remainder = divmod(current_number, i)[1]
    #             if remainder == 0:
    #                 factors.append(i)
    #                 break
    #         current_number = multiple
    #     return factors
