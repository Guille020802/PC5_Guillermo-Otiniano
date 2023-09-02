
import pandas as pd

df_airbnb = pd.read_csv('C:/Users/usuario/Downloads/airbnb.cs')
roberto_clara_df = df_airbnb[df_airbnb['room_id'].isin([97503, 90387])]

roberto_clara_df.to_excel('C:\Users\usuario\OneDrive\Escritorio\Python/roberto.xls', index=False)
