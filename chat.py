#!/bin/env python
from app import app, socketio
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,LoginManager, login_user

#app = create_app(debug=True)
#app.secret_key = 'xxxxyyyyyzzzzz'

if __name__ == '__main__':   
    socketio.run(app,debug="true",host='0.0.0.0',port=5004)
