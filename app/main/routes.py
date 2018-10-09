from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm,RegisterForm
from .model.user import User


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        session['owner'] = form.owner.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
        form.owner.data = session.get('owner', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    owner = session.get('owner', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
    
@main.route('/register', methods=['GET', 'POST'])
def register():
    """Register form."""
    form = RegisterForm()
    if request.method == 'POST':
        print("vót egy poszt kérés")
        if form.validate_on_submit():
            print("rip van")
            #hashpass =generate_password_hash(form.password.data, method='sha256')
            #    hey = User(form.email.data,hashpass).save()
            #    login_user(hey)
            User(form.name.data,form.email.data).save()
            
            #session['name'] = form.name.data
            #session['email'] = form.email.data
            #session['password'] = form.password.data
            #session['confirm'] = form.confirm.data
            return redirect(url_for('.index'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.email.data = session.get('email', '')
        form.password.data = session.get('password', '')
        form.confirm.data = session.get('confirm', '')
        print("get volt")
    print("semmi sem történt")
    return render_template('register.html', form=form)