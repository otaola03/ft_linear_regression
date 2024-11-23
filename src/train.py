import pandas as pd
import numpy as np

def compute_gradient(x, y, m_now, b_now):
    n = float(len(x))
    m_gradient = - (2/n) * np.sum(x * (y - (m_now * x + b_now)))
    b_gradient = - (2/n) * np.sum(y - (m_now * x + b_now))

    gradient = np.sqrt(m_gradient**2 + b_gradient**2)

    return (gradient)

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
    epochs = 100000

    x_mean = points['km'].mean()
    x_std = points['km'].std()
    y_mean = points['price'].mean()
    y_std = points['price'].std()
    
    points['km_normalized'] = (points['km'] - x_mean) / x_std
    points['price_normalized'] = (points['price'] - y_mean) / y_std
    
    while (compute_gradient(points['km_normalized'].values, points['price_normalized'].values, m, b) > 0.01):
        m, b = gradient_descent(m, b, points, L)

    m_original = m * (y_std / x_std)
    b_original = (b * y_std) + y_mean - m_original * x_mean

    print(f"Original m: {m_original}, Original b: {b_original}")

    return (m_original, b_original)


if __name__ == "__main__":
    data = pd.read_csv('lib/data.csv')
    train(data)
