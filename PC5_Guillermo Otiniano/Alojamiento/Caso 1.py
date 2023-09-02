
import pandas as pd

df = pd.read_csv('C:/Users/usuario/Downloads/airbnb.cs')

filtro = (df['reviews'] > 10) & (df['overall_satisfaction'] > 4) & (df['bedrooms'] >= 2)

df_filtrado = df[filtro].sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

tres_alternativas = df_filtrado.head(3)

print(tres_alternativas[['room_id', 'neighborhood', 'reviews', 'overall_satisfaction', 'bedrooms', 'price']])
