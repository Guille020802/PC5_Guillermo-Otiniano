
import pandas as pd

df_airbnb = pd.read_csv('C:/Users/usuario/Downloads/airbnb.cs')

filtro = (df_airbnb['price'] <= 50) & (df_airbnb['room_type'] == 'Shared room')

propiedades_baratas = df_airbnb[filtro].sort_values(by=['price', 'overall_satisfaction'], ascending=[True, False])

propiedades_baratas = propiedades_baratas.head(10)

print(propiedades_baratas[['room_id', 'neighborhood', 'price', 'overall_satisfaction']])