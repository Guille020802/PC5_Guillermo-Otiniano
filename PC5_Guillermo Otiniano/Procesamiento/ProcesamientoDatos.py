
import pandas as pd
import sqlite3

# Cargar los datos desde el archivo CSV
df = pd.read_csv('candidates.csv')

# Crear una conexión a la base de datos SQLite
conn = sqlite3.connect('candidates.db')

# Almacenar los datos en una tabla SQLite
df.to_sql('candidates_data', conn, if_exists='replace', index=False)

# Cerrar la conexión a la base de datos
conn.close()
