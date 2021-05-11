import pandas as pd
excel_url = 'C:\dummy\street_jr.xlsx'
# df = pd.read_excel(excel_url)
# df1 = pd.read_excel(excel_url, sheet_name = 0)
df_all = pd.read_excel(excel_url, sheet_name = None)
concatted_df = pd.concat(df_all, ignore_index=True)