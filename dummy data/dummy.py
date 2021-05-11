import random
from pymongo import mongo_client
import uuid, time
from pymongo import MongoClient 
from Fake_data import Random_data

# dummy.py 파일을 실행하면  dummy data가 생성됩니다.
# id_count는 10개의 ID갯수를 말함.
# rand_nm은 랜덤으로 2~6개의 메타태그 생성.
# 그냥 원하는 메타태그 갯수를 넣어도 됨.
# 입맛대로 고르시면 됨.

id_count = 10
rand_nm = random.randint(2,6)


#Database
client = MongoClient('localhost', 27017)
db = client.fake


for i in range(0,id_count):

# 가짜 이메일 만들고
    fk_id = Random_data().fakeId()
    user = {
        "_id" : fk_id,
        "image":[]
    }

    db.users.insert_one(user)

    # 2~6개의 메타태그가 생김
    
    for j in range(1,rand_nm):
        metatag ={
        "image_path" :str(i)+".png",
        "created_at" : Random_data().fakeTime(),
        "tag" :[Random_data().fakeAddress(), Random_data().fakeTag(), Random_data().fakeSex()]
        }

        db.users.update_one({'_id':fk_id},{'$push':{'tag':metatag}})
