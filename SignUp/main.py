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
    # return render_template('dashboard.html')
    return "signup complete"

# 고객 등록
# 미용사는 일단 제외
@app.route("/user/signup", methods=['POST'])
def signup():
  return User().signup()

@app.route('/upload', methods=['GET'])
def upload():
    return render_template('index.html')

@app.route('/upload/complete', methods=['POST'])
def upload_complete():

    # 이미지 받기
    pic = request.files['pic']

    # 이메일 검색 -> DB 찾아서 -> 파일저장
    # 예시
    email = 'hann101@naver.com'
    # email = 'kim101@naver.com'


    confirm_email = db.users.find_one({"email": email})
    #   print(db.users.find_one({"email": email_con}))
    if email in confirm_email['email']:
    #   TypeError: 'NoneType' object is not subscriptable
    #   데이터를 못가져오고있다.none으로..
    #   애초에 db에 데이터를 저장해놓지 않아서 못불러옴.
    #     # 이메일 있는지 확인
        print('이메일이 확인되었습니다. ')
    #     # 현 디렉토리에 파일명(고객이메일)이 있는지 확인
        list_check = os.listdir(current_dir)
        print(list_check)
        image_dir = current_dir + email +'\ '
        image_dir = image_dir.replace(" ", "")
        
        if email not in list_check:
            # mk_dir = current_dir + email
            #current_dir == os.getcwd() +'\SignUp\image\ '
            # mk_dir = mk_dir.replace(" ", "")
            print(image_dir)
            os.mkdir(image_dir)
            pic.save(image_dir + secure_filename(pic.filename))
            
        else:
            pic.save(image_dir + secure_filename(pic.filename)) 
            

    metatag ={
        request.form.get("key") :request.form.get("value")
        # "img_name"
    }
    # metatag ={
    # "dye" :"bbb",
    # "color" : "bbb"
    # "img_name"
    # }
    db.users.update_one({'email':email},{'$push':{'image':metatag}})
    # db.metatags.insert_one(metatag)

    return 'Img Uploaded!', 200

# 메타태그
#     # 이미지 받아서
#     pic = request.files['pic']
#     # 새로운 파일이 없으면 파일을 만들고
#     # 아니면 기존의 파일(이메일이름)에 이미지를 저장한다.
#     pic.save(current_dir + secure_filename(pic.filename))
#     pic.save(image_dir + secure_filename(pic.filename))

    # 입력한 고객과 매칭해야함..db에서 가져와야함..
    # 그리고 메타태그 붙일 때 고객의 정보에 붙어야함..
    # securename이 필요한가? 필요없을듯
        #json받아서 -> 서버 전달

# 이미지는 경로에 따로저장, 이미지 번호랑 고객 번호랑 매치, 



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