import pandas as pd
from train import train
import matplotlib.pyplot as plt

# def get_data(data):
#     return pd.read_csv(data)
#
# if __name__ == "__main__":
#     data = get_data('lib/data.csv')
#     m, b = train(data)
#     print(m, b)
#

import pandas as pd
import numpy as np

# Leer datos
points = pd.read_csv('lib/data.csv')

# Normalización (reescalar entre 0 y 1)
x_mean = points['km'].mean()
x_std = points['km'].std()
y_mean = points['price'].mean()
y_std = points['price'].std()

points['km_normalized'] = (points['km'] - x_mean) / x_std
points['price_normalized'] = (points['price'] - y_mean) / y_std

def gradient_descent(m_now, b_now, points, L):
    """
    Ejecuta una iteración del gradiente descendente para ajustar los parámetros m y b.

    Args:
        m_now (float): Pendiente actual de la línea.
        b_now (float): Intersección actual de la línea.
        points (DataFrame): Datos normalizados.
        L (float): Tasa de aprendizaje.

    Returns:
        tuple: Nuevos valores de m y b.
    """
    m_gradient = 0
    b_gradient = 0
    n = float(len(points))
    
    for i in range(len(points)):
        x = points.iloc[i]['km_normalized']
        y = points.iloc[i]['price_normalized']
        
        # Cálculo del gradiente
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    # Actualización de m y b
    m = m_now - (L * m_gradient)
    b = b_now - (L * b_gradient)
    return m, b

# Inicializar parámetros
m = 0  # Pendiente inicial
b = 0  # Intersección inicial
L = 0.1  # Tasa de aprendizaje ajustada para datos normalizados
epochs = 1000  # Número de iteraciones

# Entrenamiento con gradiente descendente
for i in range(epochs):
    m, b = gradient_descent(m, b, points, L)
    if i % 100 == 0:  # Mostrar progreso cada 100 épocas
        print(f"Epoch {i+1}: m = {m}, b = {b}")

# Desnormalización de los parámetros finales
m_original = m * (y_std / x_std)
b_original = (b * y_std) + y_mean - m_original * x_mean

# Resultados finales
print(f"Final normalized parameters: m = {m}, b = {b}")
print(f"Final original parameters: m = {m_original}, b = {b_original}")

