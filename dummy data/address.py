import pandas as pd
import random

excel_url = 'C:\\Users\\hann1\\Dummy Data\Region_name_0.csv'
df = pd.read_csv(excel_url)
df = df.drop('Unnamed: 0',axis=1)


rand_address = random.randrange(0,227)
fake_address = df.loc[[rand_address],:].values.tolist()[0][0] + ' ' + df.loc[[rand_address],:].values.tolist()[0][1]

print(fake_address)
# excel_url = 'C:\\Users\\hann1\\Dummy Data\Region_name_0.csv'
# df = pd.read_csv(excel_url)
# df = df.drop('Unnamed: 0',axis=1)

# t = []


# a = random.randrange(0,227)
# print(a)
# t.append(df.loc[[a],:].values.tolist()[0][0] + ' ' + df.loc[[a],:].values.tolist()[0][1])