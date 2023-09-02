
import pandas as pd
import matplotlib.pyplot as plt

df_airbnb = pd.read_csv('C:/Users/usuario/Downloads/airbnb.cs')

conteo_tipos_habitacion = df_airbnb['room_type'].value_counts()
colores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

plt.figure(figsize=(8, 6))
plt.pie(conteo_tipos_habitacion, labels=conteo_tipos_habitacion.index, colors=colores, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  

plt.title('Distribución de Tipos de Habitaciones (room_type)')

plt.show()
