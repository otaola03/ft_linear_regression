import pandas as pd

def gradient_descent(m, b, data, L):
    N = len(data)
    m_gradient = 0
    b_gradient = 0
    for index, row in data.iterrows():
        x_value = row['km']
        y_value = row['price']
        
        m_gradient += -(2/N) * x_value * (y_value - ((m * x_value) + b))
        b_gradient += -(2/N) * (y_value - ((m * x_value) + b))

    m = m - (L * m_gradient)
    b = b - (L * b_gradient)
    return (m, b)


def train(data):
    gradient_descent(0, 0, data, 0.0001)
