from flask_mongoengine import MongoEngine
#from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user
from chat import app

app.config['MONGODB_SETTINGS'] = {
    'db': 'cardGame',
    'host': '192.168.125.231:27017'
}
db = MongoEngine(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

class User(UserMixin, db.Document):
    meta = {'collection': 'users'}
    name = db.StringField()
    email = db.StringField()
    #token = db.StringField()
    is_confirmed = db.StringField(default="False")
    decks = db.ListField(default=["wow","balint"])
    password_hash = db.StringField()
    
    @property
    def password(self):
        raise AttributeError('cant')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(userid):
        #bi = binary.Binary(userid);
        return User.objects(email=userid).first()
