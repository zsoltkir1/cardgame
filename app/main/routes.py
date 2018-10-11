from flask import flash, session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm,RegisterForm,LoginForm2,IndexForm
#from chat import User
from app.main.user import User
from app.main.emailservice import send_email, generate_confirmation_token, confirm_token
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user
#from chat import app


#@main.route('/', methods=['GET', 'POST'])
#def index():
#    """Index page."""
#    return render_template('index.html')

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
        if form.validate_on_submit():
            user=User()
            user.name = form.name.data
            user.email = form.email.data
            user.token = generate_confirmation_token(form.email.data)
            user.password = form.password.data
            user.save()
            html=render_template("email/welcome.html", email=user.name, token=user.token)
            send_email("de.ik.ejournal@gmail.com","ejournal",user.email,"Registration",html)
            return redirect(url_for('.index'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.email.data = session.get('email', '')
        form.password.data = session.get('password', '')
        form.confirm.data = session.get('confirm', '')
    return render_template('register.html', form=form)
    
@main.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""      
    if request.method == 'POST':
        form = LoginForm2()
        if form.validate_on_submit():
            user=User.objects(email=form.email.data).first()
            if user is not None and user.verify_password(form.password.data):
                print(user.email)
                login_user(user)
                if current_user.is_confirmed == "True":
                    return render_template('loggedin.html')
                else:
                    return render_template('notActivated.html')
        return render_template('fail.html', form=form)
    elif request.method == 'GET':
        if current_user.is_authenticated:
            return render_template('loggedin.html')
        else:
            form = LoginForm2()
            return render_template('login.html', form=form)
            

@main.route('/confirm/<token>', methods=['GET', 'POST'])
def confirm_email(token):
    """Email confirmation"""      
    if request.method == 'GET':
        try:
            email = confirm_token(current_user.token)
        except:
            flash('The confirmation link is invalid or has expired.', 'danger')
        #user = User.query.filter_by(email=email).first_or_404()
        if current_user.is_authenticated:
            print (current_user.email)
            if current_user.is_confirmed == "True":
                flash('Account already confirmed.', 'success')
            elif token==current_user.token:
                current_user.is_confirmed = "True"
                current_user.save()
                #user.confirmed_on = datetime.datetime.now()
                flash('You have confirmed your account. Thanks!', 'success')
                return render_template('registered.html')
            else:
                return render_template('wrongtoken.html')
        else:
            return redirect('/login')