from flask  import Flask, render_template ,Blueprint
from user.second import second
# from flask_pymongo import Pymongo
# mongo = Pymongo()

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/user")

# #database
# app.config['MONGP_URI'] = 'mongodb+srv://hjm_user:1234@cluster0.5ed3m.mongodb.net/mydb?retryWrites=true&w=majority'
# mongo.init_app(app)
# 여기서 db가 다 막힌다...


# main = Blueprint('main', __name__)
# client = pymongo.MongoClient('localhost',27017)
# db = client.user_login_system

@app.route('/')
def hello_world():
    return render_template('home.html')
    # return 'home'

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
    # return 'dashboard'

if __name__ == "__main__":
    app.run(debug=True, port= 5000)