from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
 
bootstrap = Bootstrap() 

def create_app():

    app = Flask(__name__)

    #Creating the app configuration
    app.config.from_object(Config)

    #Initializing flask extension
    bootstrap.init_app(app)


    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting config

    from .requests import configure_request
    configure_request(app)

    #Will add the views and forms

    return app