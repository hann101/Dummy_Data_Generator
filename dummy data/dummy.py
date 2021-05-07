from pymongo import mongo_client
import uuid, time
from pymongo import MongoClient 

nowDate = time.strftime('%y-%m-%d %H:%M:%S')

client = MongoClient('localhost', 27017)
db = client.user_login_system
# email = 'hann101@naver.com'
email = 'kim101@nate.com'
# email = 'hanji101@naver.com'
name = 'han'
age = '123'
sex = 'M'
address = '서울'
phone_num = '01013'


# user = {
#     "_id" : uuid.uuid4().hex,
#     "email" : email,
#     "name" : name,
#     "age" : age,
#     "sex" : sex,
#     "address" : address,
#     "phone_num" : phone_num,
#     "created_at":nowDate
    
#     # "_id" : uuid.uuid4().hex,
#     # "name" : request.form.get('name'),
#     # "email" : request.form.get('email'),
#     # "password" : request.form.get('password')
#     #여기에 추가하면 된다.
# }


# db.users.insert_one(user)

metatag ={
"image_path" :"C://hello//"+email,
# 이미지 파일명 imagepath는 파일명으로
"dye" : "a",
"color" : "a",
# "img_name"
}

# print(db.users.find_one({"image.dye" : "a"},{"image.image_path":1}))
db.users.update_one({'email':email},{'$push':{'image':metatag}})
# db.users.update_one({'email':email},{'$push':{'image':metatag}})
# a = list(db.users.find_one({'image.dye':{"$exists":True}},{'image.image_path','image.dye'}))
# print(a)
# db.hair.find({'image.펌':{"$exists":True}},{'image.image_path','image.펌'}))









# b=list(db.hair.find({'image.펌':{"$exists":True}},{'image.image_path','image.펌'}))
# print(b)
# wow=[]
# for i in range(len(b)):
#     print(len(b))
#         if type(b[i]['image']) == list:
#         for ii in range(len(b[i]['image'])):
#             print(len(b[i]['image'][ii]))
#             if len(b[i]['image'][ii]) >=2:
#                 fu=b[i]['image'][ii]['image_path']
#                 wow.append(fu)
#                 print(b[i]['image'][ii]['image_path']) # 크기 2개임
#     if type(b[i]['image']) == dict:
#         print(b[i]['image']['image_path'])
#         uk = b[i]['image']['image_path']
#         wow.append(uk)
# print(하하)