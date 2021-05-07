import random
import pandas as pd
import numpy as np

sido_name = ['서울특별시',
'부산광역시',
'대구광역시',
'인천광역시',
'광주광역시',
'대전광역시',
'울산광역시',
'세종특별자치시',
'경기도',
'강원도',
'충청북도',
'충청남도',
'전라북도',
'전라남도',
'경상북도',
'경상남도',
'제주특별자치도']

df = pd.read_excel('C:\dummy\street_jr.xlsx', sheet_name=sido_name[1])
list_from_df = df.values.tolist()

list_from_df[4]

i = len(list_from_df)
rand_num = random.randint(1,i)
address = list_from_df[rand_num]
address_combine = sido_name[1]+' '+ address[0] +' '+ address[1]