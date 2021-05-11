
import pandas as pd
import random
import os
# 랜던 주소 만들기 완료

class Random_data:
    def fakeAddress(self):
        excel_url = os.getcwd()+'\\Region_name_0.csv'
        df = pd.read_csv(excel_url)
        df = df.drop('Unnamed: 0',axis=1)

        rand_address = random.randrange(0,227)
        fake_address = df.loc[[rand_address],:].values.tolist()[0][0] + ' ' + df.loc[[rand_address],:].values.tolist()[0][1]

        return fake_address


    def fakeId(self):
        excel_url = os.getcwd()+'\\MOCK_DATA.csv'
        df = pd.read_csv(excel_url)

        i = random.randrange(1,1000)

        df_list = df.values.tolist()
        User_id = df_list[i][0].split('@')[0]
        return User_id

    def fakeTag(self):
        
        f = open("s1.txt", 'r',encoding='utf-8')
        lines = f.readlines()
        hair_line = []
        for line in lines:
            line = line.replace('\n','')
            hair_line.append(line)
        f.close()
        # a = random.randrange(1,7)

        b = (random.choice(hair_line))
        return b
    
    def fakeTime(self):
        rand_yr = random.randrange(2016,2021)
        rand_mth= random.randrange(1,12)
        rand_date = random.randrange(1,30)
        nowDate = str(rand_yr)+ '-' +str(rand_mth) + '-'+ str(rand_date)
        return nowDate

    def fakeSex(self):
        sex_list = ['M','F']
        sex = random.choice(sex_list)
        return sex

