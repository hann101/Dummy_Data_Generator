from flask import Flask

from .main import main
from signup.user.second import second

from .extenstion import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGP_URI'] = 'mongodb+srv://hjm_user:1234@cluster0.5ed3m.mongodb.net/mydb?retryWrites=true&w=majority'
    
    mongo.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(second, url_prefix="/user")
    
    return app


