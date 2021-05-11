
import pandas as pd
import random
# excel_url = 'C:\Flask_Test\dummy data\MOCK_DATA.csv'
# df = pd.read_csv(excel_url)
# # print(df)
# for i in range(1,10):
#     df_list = df.values.tolist()
#     User_id = df_list[i][0].split('@')[0]
#     print(User_id)

excel_url = 'C:\Flask_Test\dummy data\MOCK_DATA.csv'
df = pd.read_csv(excel_url)
# print(df)

i = random.randrange(1,1000)

df_list = df.values.tolist()
User_id = df_list[i][0].split('@')[0]
print(User_id)
