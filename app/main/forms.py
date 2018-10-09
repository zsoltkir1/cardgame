from flask_wtf import Form
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    name = StringField('Név', validators=[Required()])
    room = StringField('Szoba', validators=[Required()])
    owner = StringField('Pakli', validators=[Required()])
    submit = SubmitField('Belépek')

class RegisterForm(Form):
    name = StringField('Name', validators=[Required()])
    email = StringField('E-mail', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    confirm = PasswordField('Password again', validators=[Required()])
    submit = SubmitField('Register User')    