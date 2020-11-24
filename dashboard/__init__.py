from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
from dashboard.config import Config
from flask_googlemaps import GoogleMaps
from flask_wkhtmltopdf import Wkhtmltopdf
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'

cwd = os.getcwd()
UPLOAD_FOLDER = '/var/www/Mizani/dashboard/static/img/'
# UPLOAD_FOLDER = '/Users/ahmedk/Desktop/Farmula/Mizani/Dashboard/dashboard/static/img/' 

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static',
            template_folder='templates')
    app.config.from_object(Config)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from dashboard.category.routes import category
    from dashboard.collection.routes import collection
    from dashboard.producttype.routes import producttype
    from dashboard.concerns.routes import concerns
    from dashboard.size.routes import size
    from dashboard.role.routes import role
    from dashboard.users.routes import users
    from dashboard.product.routes import product
    from dashboard.status.routes import status
    from dashboard.main.routes import main 

    # from dashboard import routes
    app.register_blueprint(category)
    app.register_blueprint(collection)
    app.register_blueprint(producttype)
    app.register_blueprint(size)
    app.register_blueprint(concerns)
    app.register_blueprint(users)
    app.register_blueprint(status)
    app.register_blueprint(product)
    app.register_blueprint(main)

    return app
    