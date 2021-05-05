from flask import Blueprint,render_template,jsonify,request
from werkzeug.utils import secure_filename
import os
from pymongo import MongoClient 

upload_bp = Blueprint('upload', __name__, url_prefix='/upload')

@upload_bp.route('/', methods=['GET'])
def upload():
    return render_template('index.html')
    # return 'upload'

@upload_bp.route('/complete', methods=['POST'])
def upload_complete():
    current_dir = os.getcwd() +'\SignUp\image\ '
    current_dir = current_dir.replace(" ", "")
    client = MongoClient('localhost', 27017)
    db = client.user_login_system
    # 이미지 받기
    pic = request.files['pic']
    # 이메일 검색 -> DB 찾아서 -> 파일저장
    # 예시
    email = 'hann101@naver.com'
    # email = 'kim101@naver.com'
    # email = 'kimm101@naver.com'



    confirm_email = db.users.find_one({"email": email})
    if email in confirm_email['email']:
    #   TypeError: 'NoneType' object is not subscriptable
    #   데이터를 못가져오고있다.none으로..
    #   애초에 db에 데이터를 저장해놓지 않아서 못불러옴.
        print('이메일이 확인되었습니다. ')
    # 현 디렉토리에 파일명(고객이메일)이 있는지 확인
        list_check = os.listdir(current_dir)
    # image_dir  ->   C:\Flask_Test\SignUp\image\kimm101@naver.com\
    # current_dir  -> C:\Flask_Test\SignUp\image\
        image_dir = current_dir + email +'\ '
        image_dir = image_dir.replace(" ", "")
        if email not in list_check:
            # 해당 이메일의 폴더가 없으면 새로운 폴더를 만들고, 해당 이미지를 저장
            mk_dir = current_dir + email
            #current_dir == os.getcwd() +'\SignUp\image\ '
            mk_dir = mk_dir.replace(" ", "")
            # mk_dir이랑 image_dir은 \ 표기 붙냐 안붙야에 따라 파일 디렉토리가 구분되는것
            # 파일 이름 만드는 거는 함수로 한번에 정리하는게 깕글할듯]
            os.mkdir(mk_dir)
            num_of_png = len(os.listdir(image_dir)) +1
            num_of_png = str(num_of_png)
            # # 1개 파일이 있으면 2가 들어감
            new_filename = num_of_png + '.png'
            new_filename = str(new_filename)
            pic.save(image_dir + new_filename)

        # db.users.insert_one({'name':'john','image':[{"file_name" : "picture.png","file_name" : "picture_1.png" }]})

        else:
            # 1개 파일이 있으면 2가 들어감
            num_of_png = len(os.listdir(image_dir)) +1
            print(num_of_png)
            num_of_png = str(num_of_png)
            new_filename = num_of_png + '.png'
            new_filename = str(new_filename)
            pic.save(image_dir + new_filename) 
                
            # image_dir  ->   C:\Flask_Test\SignUp\image\kimm101@naver.com\
            # current_dir  -> C:\Flask_Test\SignUp\image\

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

    return 'Img Uploaded!', 200

