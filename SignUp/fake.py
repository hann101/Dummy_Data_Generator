from flask  import Flask, render_template,jsonify,request
from werkzeug.utils import secure_filename
from passlib.hash import pbkdf2_sha256
import os
# from user.second import second
import uuid

from pymongo import MongoClient 
client = MongoClient('localhost', 27017)
db = client.designer_login_system

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



class Designer:
    # def start_session(self, designer):
    #     session['logged_in'] = True
    #     session['designer'] = designer
    #     return jsonify(designer), 200
    
    # 회원 정보 등록 (기본정보)------------------------------
    # 회원 개인정보 등록하는 컬럼
    def signup(self):
        print(request.form)

        # 사용자 객체 생성
        designer = {
            "_id" : uuid.uuid4().hex,
            "name" : request.form.get('name'),
            "email" : request.form.get('email'),
            "password" : request.form.get('password')
            #여기에 추가하면 된다.
        }

        designer['password'] = pbkdf2_sha256.encrypt(designer['password'])
        
        
        
        if db.designers.find_one({"email": designer['email']}):
            return jsonify({"error":"Email address already in use"}), 400
            # 경고가 안나옴..

        else:
            db.designers.insert_one(designer)
            return "Complete", 200
        
        # return jsonify({"error": "SignUp failed"})
            
            # db.designers.insert_one({'name':'john','age':[{"chat" : "Bravo","message" : "Hey Man!" }]})



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

# 미용사 회원가입
@app.route("/designer/signup", methods=['POST'])
def signup():
  return Designer().signup()

@app.route('/upload', methods=['GET'])
def upload():
    return render_template('index.html')

@app.route('/upload/complete', methods=['POST'])
def upload_complete():
    pic = request.files['pic']
    pic.save(current_dir + secure_filename(pic.filename))

    #json받아서 -> 서버 전달
    metatag ={
        request.form.get("key") :request.form.get("value")
        "img_name"
    }
# 이미지는 경로에 따로저장, 이미지 번호랑 고객 번호랑 매치, 
    db.metatags.insert_one(metatag)




    # 입력한 고객과 매칭해야함..db에서 가져와야함..
    # 그리고 메타태그 붙일 때 고객의 정보에 붙어야함..
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