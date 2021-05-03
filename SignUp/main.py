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
# def changeName(path, cName, num_of_png):
    
#     for filename in os.listdir(path):
#         print(path+filename, '=>', path+str(cName)+str(num_of_png)+'.png')
#         os.rename(path+filename, path+str(cName)+str(num_of_png)+'.png')
       


class User:
    # 회원 정보 등록 (기본정보)
    # 회원 개인정보 등록하는 컬럼
    def signup(self):
        print(request.form)

        # 사용자 객체 생성
        user = {
            "_id" : uuid.uuid4().hex,
            "email" : request.form.get('email'),
            "name" : request.form.get('name'),
            "age" : request.form.get('age'),
            "sex" : request.form.get('sex'),
            "address" : request.form.get('address'),
            "phone_num" : request.form.get('phone_num')
            # "created_at":nowDate
            # "_id" : uuid.uuid4().hex,
            # "name" : request.form.get('name'),
            # "email" : request.form.get('email'),
            # "password" : request.form.get('password')
            #여기에 추가하면 된다.
        }

        # user['password'] = pbkdf2_sha256.encrypt(user['password'])
        db.users.insert_one(user)
        # db.users.insert_one({'name':'john','image':[{"file_name" : "picture.png","file_name" : "picture_1.png" }]})

        return jsonify(user), 200



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
    print(type(pic.filename))
    print(pic)
    # 이메일 검색 -> DB 찾아서 -> 파일저장
    # 예시
    # email = 'hann101@naver.com'
    # email = 'kim101@naver.com'
    email = 'kimm101@naver.com'



    confirm_email = db.users.find_one({"email": email})
    #   print(db.users.find_one({"email": email_con}))
    if email in confirm_email['email']:
    #   TypeError: 'NoneType' object is not subscriptable
    #   데이터를 못가져오고있다.none으로..
    #   애초에 db에 데이터를 저장해놓지 않아서 못불러옴.
    #     # 이메일 있는지 확인
        print('이메일이 확인되었습니다. ')

        #파일 이름 변경




    #     # 현 디렉토리에 파일명(고객이메일)이 있는지 확인
        list_check = os.listdir(current_dir)
        print(list_check)
        image_dir = current_dir + email +'\ '
        image_dir = image_dir.replace(" ", "")


        print(current_dir)
        print(image_dir)
        print(os.listdir(image_dir))




        # image_dir  ->   C:\Flask_Test\SignUp\image\kimm101@naver.com\
        # current_dir  -> C:\Flask_Test\SignUp\image\
        # 해당 이메일의 파일 갯수 +1 ==create_png_num


        # # 이미지 이름바꾸기..
        # create_png_num = len(os.listdir(image_dir)) + 1
        # if os.listdir(image_dir)
        # # create_png_num = str(create_png_num)
        #     print(create_png_num)
        #     print(type(create_png_num))

        # for filename in os.listdir(image_dir) :
        #     # 1.png,2.png
        #     filename.
        #     if filename is not
        #     print(path+filename, '=>', path+str(cName)+str(create_png_num)+'.png')
        #     os.rename(path+filename, path+str(cName)+str(create_png_num)+'.png') 
        



        if email not in list_check:
            # 해당 이메일의 폴더가 없으면 새로운 폴더를 만들고, 해당 이미지를 저장
            # mk_dir = current_dir + email
            #current_dir == os.getcwd() +'\SignUp\image\ '
            # mk_dir = mk_dir.replace(" ", "")
            print(image_dir)
            # os.mkdir(image_dir)
            # # pic.save(image_dir + secure_filename(pic.filename))
            # os.rename(path+filename, path+str(cName)+str(i)+'.jpg')
            # changeName(image_dir,email ,num_of_png)
            # #

        # db.users.insert_one({'name':'john','image':[{"file_name" : "picture.png","file_name" : "picture_1.png" }]})



        #파일 이름 변경
        # num_of_png = len(os.listdir(current_dir)) + 1
        # num_of_png = str(num_of_png) +'.png'
        # print(num_of_png)
        # print(type(num_of_png))

        # def changeName(path, cName, create_png_num):
        # if os.listdir(image_dir)


            
        else:
            pic.save(image_dir + secure_filename(pic.filename)) 
            # changeName(image_dir,email,create_png_num)

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
    # 순서, 생성일시 등이 있으면 좋겠다~
    # db.metatags.insert_one(metatag)
    # db.users.update_one({'email':email},{'$push':{'image':'1'}})

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