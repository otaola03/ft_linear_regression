import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button



def compute_gradient(x, y, m_now, b_now):
    n = float(len(x))
    m_gradient = - (2/n) * np.sum(x * (y - (m_now * x + b_now)))
    b_gradient = - (2/n) * np.sum(y - (m_now * x + b_now))

    gradient = np.sqrt(m_gradient**2 + b_gradient**2)

    return (gradient)


def gradient_descent(m_now, b_now, x, y, L):
    n = float(len(x))
    
    m_gradient = - (2/n) * np.sum(x * (y - (m_now * x + b_now)))
    b_gradient = - (2/n) * np.sum(y - (m_now * x + b_now))
    
    m = m_now - (L * m_gradient)
    b = b_now - (L * b_gradient)
    
    return m, b


def normalize(x_mean, x_std, y_mean, y_std, points):
    km_normalized = ((points['km'] - x_mean) / x_std).values
    price_normalized = ((points['price'] - y_mean) / y_std).values
    
    return km_normalized, price_normalized


def denormalize(x_mean, x_std, y_mean, y_std, m, b):
    m_original = y_std * m / x_std
    b_original = y_std * b + y_mean - m_original * x_mean
    
    return m_original, b_original


def train(points, m=0, b=0, L=0.0001, epsilon=0.0001 , line_plot=None):
    x_mean = points['km'].mean()
    x_std = points['km'].std()
    y_mean = points['price'].mean()
    y_std = points['price'].std()
    
    km_normalized, price_normalized = normalize(x_mean, x_std, y_mean, y_std, points)
    
    i = 0
    while (compute_gradient(km_normalized, price_normalized, m, b) > epsilon):
        m, b = gradient_descent(m, b, km_normalized, price_normalized, L)
        if i % 50 == 0:
            denormalize_m, denormalize_b = denormalize(x_mean, x_std, y_mean, y_std, m, b)
            line_plot = update_line(points, denormalize_m, denormalize_b, line_plot)
        i += 1

    m_original, b_original = denormalize(x_mean, x_std, y_mean, y_std, m, b)

    return (m_original, b_original)


def update_data(data, m, b):
    df = pd.read_csv('lib/line_data.csv')
    df.loc[0, 'm'] = float(m)
    df.loc[0, 'b'] = float(b)
    df.to_csv('lib/line_data.csv', index=False)

#------------------ PLOT ------------------#

def on_click(event, data, m, b, line_plot):
    print('Training...')
    new_m, new_b = train(data, m, b, L=0.01, epsilon=0.0001, line_plot=line_plot)
    update_data(data, new_m, new_b)
    print(new_m, new_b)


def crete_plot(data, m, b):
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]

    plt.scatter(x, y, label='Data points', color='blue')

    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Price of a car according to its km')

    y_line = m * x + b
    line_plot, = plt.plot(x, y_line, label=f'y = {m}x + {b}', color='red')

    plt.legend()

    ax_button = plt.axes([0.8, 0.05, 0.15, 0.075])
    button = Button(ax_button, 'Train')
    button.on_clicked(lambda event: on_click(event, data, m, b, line_plot))

    plt.show()

    return (line_plot)


def update_line(data, m, b, line_plot):
    x = data.iloc[:, 0]

    y_line = m * x + b 

    line_plot.set_ydata(y_line)
    line_plot.set_label(f"y = {m:.3f}x + {b:.3f}")
    line_plot.axes.legend()

    plt.draw()
    plt.pause(0.1)
    return line_plot


if __name__ == "__main__":
    data = pd.read_csv('lib/data.csv')
    m = 0
    b = 0

    line_plot = crete_plot(data, m, b)
    plt.show()

