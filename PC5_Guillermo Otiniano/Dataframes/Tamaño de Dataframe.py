#Pregunta 1

import pandas as pd

ruta_del_archivo = 'C:/Usuarios/usuario/Descargas/avengers.csv'
avengers = pd.read_csv(ruta_del_archivo)

tamanio = avengers.shape
print("Número de filas y columnas:", tamanio)