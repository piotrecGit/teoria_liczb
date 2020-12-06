from flask_wtf import FlaskForm, RecaptchaField
from wtforms import IntegerField, SubmitField
from wtforms.validators import *


class EuklidesForm(FlaskForm):
    a = IntegerField('Liczba a')
    b = IntegerField('Liczba b')
    submit = SubmitField('Oblicz')


class PrimesForm(FlaskForm):
    od = IntegerField('Zakres od (min. 1999900000):', [NumberRange(min=1999900000, max=2000099990, message='Liczba "od" jest spoza zakresu <1999900000, 2000099990>')])
    do = IntegerField('Zakres do (max. 2000099990):', [NumberRange(min=1999900000, max=2000099990, message='Liczba "do" jest spoza zakresu <1999900000, 2000099990>')])
    submit = SubmitField('Znajdź liczby pierwsze')


class FactorizationForm(FlaskForm):
    liczba = IntegerField('Liczba:', [NumberRange(min=2, max=2000099990, message='Liczba musi być większa od 1 i mniejsza od 2000099991')])
    submit = SubmitField('Rozłóż na czynniki pierwsze')


class FermatTestForm(FlaskForm):
    liczba = IntegerField('Liczba:', [NumberRange(min=2, message='Liczba musi być większa od 1')])
    dokladnosc = IntegerField('Dokładność testu (od 1 do ...):', [NumberRange(min=1, message='Liczba musi być większa od 0')])
    submit = SubmitField('Wykonaj Test')


class EulerFunctionForm(FlaskForm):
    liczba = IntegerField('Liczba:', [NumberRange(min=2, message='Liczba musi być większa od 1')])
    submit = SubmitField('Oblicz')


