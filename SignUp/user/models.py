from flask import Flask,jsonify,request
from passlib.hash import pbkdf2_sha256
import time

from pymongo import MongoClient 
client = MongoClient('localhost', 27017)
db = client.user_login_system
nowDate = time.strftime('%y-%m-%d %H:%M:%S')

# 이 문장을 넣으니깐 오류가 발생함... 
# ImportError: cannot import name 'User' from partially initialized module 'user.models' (most likely due to a circular import) 이 내용,,,
import uuid

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
            "phone_num" : request.form.get('phone_num'),
            "created_at":nowDate
            
            # "_id" : uuid.uuid4().hex,
            # "name" : request.form.get('name'),
            # "email" : request.form.get('email'),
            # "password" : request.form.get('password')
            #여기에 추가하면 된다.
        }

        user['phone_num'] = pbkdf2_sha256.hash(user['phone_num'])
        db.users.insert_one(user)
        # db.users.insert_one({'name':'john','image':[{"file_name" : "picture.png","file_name" : "picture_1.png" }]})

        return jsonify(user), 200

