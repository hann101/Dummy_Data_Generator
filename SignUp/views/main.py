from flask import Blueprint,render_template
from flask import Flask
# from flask_pymongo import PyMongo
# from SignUp.extentions import mongo


main_bp = Blueprint('main', __name__, url_prefix='/')    
    
# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/user_login_system"
# mongo = PyMongo(app)

@main_bp.route('/')
def hello_world():
    return render_template('home.html')
