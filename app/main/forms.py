from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    name = StringField('Név', validators=[Required()])
    room = StringField('Room', validators=[Required()])
    submit = SubmitField('Belépek')
