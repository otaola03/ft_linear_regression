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
        x = points.iloc[i, 0]
        y = points.iloc[i, 1]
        print(f"x: {x}, y: {y}")
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    m = m_now - L * m_gradient
    b = b_now - L * b_gradient
    return [m, b]


def train(data, L=0.0001):
    m = 0
    b = 0
    print(data)
    for i in range(10):
        m, b = gradient_descent(m, b, data, L)
    return (m, b)
