from flask import Flask
from flask_socketio import SocketIO
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,LoginManager, login_user

socketio = SocketIO()
#manage_session=False

#def create_app(debug=False):
app = Flask(__name__)
#app.debug = debug

#app.host="0.0.0.0"
#app.port=5000
app.config['SECRET_KEY'] = 'krisz_egy_csicska_xD'

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


socketio.init_app(app)
#    return app

