from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import *

class EuklidesForm(FlaskForm):
    """Contact form."""
    a = IntegerField('Liczba a')
    b = IntegerField('Liczba b')
    submit = SubmitField('Oblicz')


class ContactForm(FlaskForm):
    """Example contact form."""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message=('Not a valid email address.')), DataRequired()])
    body = StringField('Message', [DataRequired(), Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
