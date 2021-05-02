from flask  import Flask, render_template,jsonify,request
from werkzeug.utils import secure_filename
from passlib.hash import pbkdf2_sha256
import os
# from user.second import second
import uuid

from pymongo import MongoClient 
client = MongoClient('localhost', 27017)
db = client.user_login_system

# 현재 위치 저장
current_dir = os.getcwd() +'\SignUp\image\ '
current_dir = current_dir.replace(" ", "")


app = Flask(__name__)
# app.register_blueprint(second, url_prefix="/user")

# #database
# app.config['MONGP_URI'] = 'mongodb+srv://hjm_user:1234@cluster0.5ed3m.mongodb.net/mydb?retryWrites=true&w=majority'
# mongo.init_app(app)
# 여기서 db가 다 막힌다...
# C:\Flask_Test\SignUp\image



class User:
    # 회원 정보 등록 (기본정보)
    # 회원 개인정보 등록하는 컬럼
    def signup(self):
        print(request.form)

        # 사용자 객체 생성
        user = {
            "_id" : uuid.uuid4().hex,
            "name" : request.form.get('name'),
            "email" : request.form.get('email'),
            "password" : request.form.get('password')
            #여기에 추가하면 된다.
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        db.users.insert_one(user)
        db.users.insert_one({'name':'bobby','age':21})
        db.users.insert_one({'name':'kay','age':27})
        db.users.insert_one({'name':'john','age':30})
        db.users.insert_one({'name':'john','age':[{"chat" : "Bravo","message" : "Hey Man!" }]})

        return jsonify(user), 200

# class User:
#     # 회원 정보 등록 (기본정보)
#     # 회원 개인정보 등록하는 컬럼
#     def signup(self):
#         print(request.form)

#         # 사용자 객체 생성
#         user = {
#             "_id" : uuid.uuid4().hex,
#             "name" : request.form.get('name'),
#             "email" : request.form.get('email'),
#             "password" : request.form.get('password')
#             #여기에 추가하면 된다.
#         }

#         user['password'] = pbkdf2_sha256.encrypt(user['password'])
#         db.users.insert_one(user)
#         db.users.insert_one({'name':'bobby','age':21})
#         db.users.insert_one({'name':'kay','age':27})
#         db.users.insert_one({'name':'john','age':30})
#         db.users.insert_one({'name':'john','age':[{"chat" : "Bravo","message" : "Hey Man!" }]})

#         return jsonify(user), 200



@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


@app.route("/user/signup", methods=['POST'])
def signup():
  return User().signup()

@app.route('/upload', methods=['GET'])
def upload():
    return render_template('index.html')
    
@app.route('/upload/complete', methods=['POST'])
def upload_complete():
    pic = request.files['pic']
    pic.save(current_dir + secure_filename(pic.filename))
    return 'Img Uploaded!', 200

#이미지, 메타태그
# @app.route('/upload', methods=['GET']) 
# def upload():
#     return render_template('index.html')


# @app.route('/upload/complete', methods=['POST']) 
# def upload_complete():
#     pic = request.files['pic']
#     print(current_dir)
#     pic.save(current_dir  + secure_filename(pic.filename))
#     return 'Img Uploaded!', 200


@app.route("/user/test")
def test():
  return "test!!!!!"

if __name__ == "__main__":
    app.run(debug=True, port= 5000)