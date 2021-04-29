from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail

# INSTANTIATE BOOTSTRAP
bootstrap = Bootstrap()

# INSTANTIATE SDB CONNECTION
db = SQLAlchemy()

# INSTANTIATED CONFIGURING AUTHENTICATION MANAGER
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# INSTANTIATED MEDIA UPLOAD AND CONFIGURED TO UPLOAD IMAGES
photos = UploadSet('photos', IMAGES)

# INSTANTIATED MAIL HANDLER
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    
    # INSTANTIATED APP CONFIGURATION ENVIRONMENT
    app.config.from_object(config_options[config_name])
    
    # INSTANTIATED APP EXTENSIONS 
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app, photos)
    mail.init_app(app)
    
    
    # REGISTERED MAIN BLUEPRINT
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # REGISTERED AUTH BLUEPRINT
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app