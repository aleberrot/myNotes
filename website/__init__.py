from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login  import LoginManager
import os

app  = Flask(__name__)
db = SQLAlchemy()
bcrypt: Bcrypt = Bcrypt(app)
DB_NAME = 'database.db'
login_manager = LoginManager(app)

def create_app():
    '''
    This function creates de app
    '''
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_NAME)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

def create_database(app):
    '''
    This function verifies if the database exists, if it is prints 'Database already created!' otherwise it creates a new instance of the database
    '''
    if not os.path.exists('instance/database.db'):
        with app.app_context():
            db.create_all()
        print('Created Database!')
    else:
        print('Database already exists')