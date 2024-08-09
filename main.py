import pandas as pd

# Cargar el archivo Excel
archivo_excel = 'lista.xlsx'
df = pd.read_excel(archivo_excel)

# Convertir la columna 'fechaActivacion' al formato deseado
df['fBlanco'] = pd.to_datetime(df['fBlanco'], format='%m/%d/%Y').dt.strftime('%Y%m%d')
df['fClaro'] = pd.to_datetime(df['fClaro'], format='%m/%d/%Y').dt.strftime('%Y%m%d')
df['fOscuro'] = pd.to_datetime(df['fOscuro'], format='%m/%d/%Y').dt.strftime('%Y%m%d')

# Guardar el DataFrame modificado en un nuevo archivo Excel
archivo_salida = 'lista2.xlsx'
df.to_excel(archivo_salida, index=False)

print("Conversión completada y guardada en", archivo_salida)
