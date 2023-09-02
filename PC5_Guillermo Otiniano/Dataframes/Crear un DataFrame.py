#Pregunta 1

import pandas as pd
df = pd.DataFrame()

print(df)

#Pregunta 2

import pandas as pd

df = pd.DataFrame()
serie_numeros = pd.Series([10, 20, 10])
df['Números'] = serie_numeros

print(df)

#Pregunta 3

import pandas as pd

df = pd.DataFrame()
serie_numeros = pd.Series([10, 20, 10])
df['Números'] = serie_numeros
serie_colores = pd.Series(['rojo', 'verde', 'azul'])
df['Colores'] = serie_colores

print(df)