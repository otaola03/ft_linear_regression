import pandas as pd
import numpy as np

def gradient_descent(m_now, b_now, points, L):
    n = float(len(points))
    
    x = points['km_normalized'].values
    y = points['price_normalized'].values
    
    m_gradient = - (2/n) * np.sum(x * (y - (m_now * x + b_now)))
    b_gradient = - (2/n) * np.sum(y - (m_now * x + b_now))
    
    m = m_now - (L * m_gradient)
    b = b_now - (L * b_gradient)
    
    return m, b


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
        if i % 100 == 0:
            print(f"Epoch {i+1}: m = {m}, b = {b}")

    m_original = m * (y_std / x_std)
    b_original = (b * y_std) + y_mean - m_original * x_mean

    return (m_original, b_original)
