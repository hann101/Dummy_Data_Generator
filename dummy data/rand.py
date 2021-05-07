import pandas as pd
df = pd.read_excel('C:\street.xls')
df = df.drop(['부여사유'],axis=1)
df.to_csv('sample.csv')