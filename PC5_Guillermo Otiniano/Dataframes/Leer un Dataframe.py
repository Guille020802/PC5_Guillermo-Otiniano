# Pregunta 1

import pandas as pd

ruta_del_archivo = 'C:/Usuarios/usuario/Descargas/avengers.csv'
avengers = pd.read_csv(ruta_del_archivo)

#Pregunta 2

cinco_filas = avengers.head(5)
print(cinco_filas)

#Pregunta 3

diez_filas = avengers.head(10)
print(diez_filas)

#Pregunta 4

ultimas_cinco_filas = avengers.tail(5)
print(ultimas_cinco_filas)
