'''from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, validators
from wtforms.validators import DataRequired
#from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, url_for, abort, flash
from model.user import User
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user
from flask.views import MethodView, request
#from app import app
#from emailservice import send_email, generate_confirmation_token, confirm_token, Confirm_Email
#from itsdangerous import URLSafeSerializer, BadSignature, URLSafeTimedSerializer

class Register(MethodView):

    def get(self):
        if current_user.is_authenticated:
            return render_template('loggedin.html')
        else:
            form = RegisterForm()
            return render_template('register.html', form=form)

    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            if len(form.name.data) < 5 or len(form.name.data) > 25 or len(form.password.data) < 5 or len(
                    form.password.data) > 25:
                return render_template('wronglength.html', form=form)
            if "@" not in form.email.data:
                return render_template('wrongemail.html', form=form)
            if form.password.data != form.confirm.data:
                return render_template('notequalpassword.html', form=form)
            user = User()
            user.name = form.name.data
            user.email = form.email.data
            user.token = generate_confirmation_token(form.email.data)
            user.password = form.password.data
            token=user.token
            #user.abilities.append("user") #not used cuz it's default
            exsisting = User.objects(email=form.email.data).first()
            if 1==2:#exsisting is not None:
                form = RegisterForm2();
                #form.email=StringField('E-mail already in use please re enter', render_kw={"placeholder": "Enter Your E-mail Address..."})
                return render_template('login3.html',form=form)
            else:
                user.save()
                #Email sending test
                html=render_template("email/welcome.html", email=user.name, token=user.token)
                send_email("de.ik.ejournal@gmail.com","ejournal",user.email,"Registration",html)
                return redirect('/')'''