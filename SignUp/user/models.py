from flask import Flask,jsonify,request
from passlib.hash import pbkdf2_sha256
from main import db

# 이 문장을 넣으니깐 오류가 발생함... 
# ImportError: cannot import name 'User' from partially initialized module 'user.models' (most likely due to a circular import) 이 내용,,,
import uuid

class Designer:
    # 회원 정보 등록
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

        designer['password'] = pbkdf2_sha256.encrypt(user['password'])
        db.users.insert_one(user)

        return jsonify(user), 200
    
    #키 벨류 자유롭게 등혹하는 거