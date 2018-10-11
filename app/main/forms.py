from flask_wtf import Form
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required


class LoginForm(Form): #valójában ez nem loginhoz hanem szobába való belépéshez kell
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
    
class LoginForm2(Form):
    email = StringField('E-mail', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Keep me logged in')
    submit = SubmitField('Login')
    
class IndexForm(Form): #ezen még elég sok változtatás lesz
    submit = SubmitField('Login')
    submit2 = SubmitField('Register')