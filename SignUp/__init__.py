from flask import Flask
# from .extentions import mongo

def create_app():
    app = Flask(__name__)

    # from pymongo import MongoClient 
    # client = MongoClient('localhost', 27017)
    # db = client.user_login_system
    # from flask_pymongo import PyMongo
    # app.config["MONGO_URI"] = "mongodb://localhost:27017/user_login_system"
    # mongo = PyMongo(app)
    # mongo.init_app(app)

    from.views import main
    app.register_blueprint(main.main_bp)


    from.user import routes
    app.register_blueprint(routes.bp)

    from .upload import routes
    app.register_blueprint(routes.upload_bp)

    
    return app


