import pandas as pd

# def gradient_descent(m, b, data, L):
#     N = len(data)
#     m_gradient = 0
#     b_gradient = 0
#     for index, row in data.iterrows():
#         x_value = row['km']
#         y_value = row['price']
#         
#         print(f"x_value: {x_value}, y_value: {y_value}")
#         m_gradient += -(2/N) * x_value * (y_value - ((m * x_value) + b))
#         b_gradient += -(2/N) * (y_value - ((m * x_value) + b))
#
#         # print(f"m_gradient: {m_gradient}, b_gradient: {b_gradient}")
#
#     m = m - (L * m_gradient)
#     b = b - (L * b_gradient)
#     return (m, b)

def gradient_descent(m_now, b_now, points, L):
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

# def normalize(points):
#     return points


def train(points, L=0.0001):
    m = 0
    b = 0
    L = 0.1
    epochs = 1000

    x_mean = points['km'].mean()
    x_std = points['km'].std()
    y_mean = points['price'].mean()
    y_std = points['price'].std()
    
    points['km_normalized'] = (points['km'] - x_mean) / x_std
    points['price_normalized'] = (points['price'] - y_mean) / y_std
    # points = normalize(points)
    
    for i in range(epochs):
        m, b = gradient_descent(m, b, points, L)
        if i % 100 == 0:  # Mostrar progreso cada 100 épocas
            print(f"Epoch {i+1}: m = {m}, b = {b}")

    m_original = m * (y_std / x_std)
    b_original = (b * y_std) + y_mean - m_original * x_mean
    return (m_original, b_original)
