import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('lib/data.csv')

# Ver las primeras filas del archivo CSV para entender la estructura
print(df.head())

# Supongamos que tienes dos columnas: 'x' y 'y' para graficar
# Cambia los nombres de las columnas por los que tengas en tu CSV
x = df['km']  # Reemplaza con el nombre de la columna para el eje X
y = df['price']  # Reemplaza con el nombre de la columna para el eje Y

# Crear el gráfico
plt.plot(x, y)

# Agregar etiquetas y título
plt.xlabel('Nombre del Eje X')
plt.ylabel('Nombre del Eje Y')
plt.title('Título de tu gráfico')

# Mostrar el gráfico
plt.show()
