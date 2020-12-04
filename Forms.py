from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class EuklidesForm(FlaskForm):
    """Contact form."""
    a = IntegerField('Liczba a', [DataRequired()])
    b = IntegerField('Liczba b', [DataRequired()])
    submit = SubmitField('Oblicz')


class ContactForm(FlaskForm):
    """Example contact form."""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message=('Not a valid email address.')), DataRequired()])
    body = StringField('Message', [DataRequired(), Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
