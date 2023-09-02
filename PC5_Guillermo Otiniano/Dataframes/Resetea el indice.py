
import pandas as pd

ruta_del_archivo = 'C:/Usuarios/usuario/Descargas/avengers.csv'
avengers = pd.read_csv(ruta_del_archivo)

avengers = avengers.reset_index(drop=True)
