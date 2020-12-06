from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import *

class EuklidesForm(FlaskForm):
    """Euklides form."""
    a = IntegerField('Liczba a')
    b = IntegerField('Liczba b')
    submit = SubmitField('Oblicz')


class PrimesForm(FlaskForm):
    """Primes form."""
    od = IntegerField('Zakres od (min. 1999900000):')#, [NumberRange(min=1999900000, max=2000099990, message='Liczba "od" jest spoza zakresu <1999900000, 2000099990>')])
    do = IntegerField('Zakres do (max. 2000099990):')#, [NumberRange(min=1999900000, max=2000099990, message='Liczba "do" jest spoza zakresu <1999900000, 2000099990>')])
    submit = SubmitField('Znajdź liczby pierwsze')


class FactorizationForm(FlaskForm):
    """Primes form."""
    liczba = IntegerField('Liczba:', [NumberRange(min=2, message='Liczba musi być większa od 1')])
    submit = SubmitField('Rozłóż na czynniki pierwsze')


class ContactForm(FlaskForm):
    """Example contact form."""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message=('Not a valid email address.')), DataRequired()])
    body = StringField('Message', [DataRequired(), Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
