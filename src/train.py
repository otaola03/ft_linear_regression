import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import Button

def total_error(m, b, x, y):
    total_error = np.sum((y - (m * x + b))**2)
    return total_error / float(len(x))

def compute_gradient(x, y, m_now, b_now):
    n = float(len(x))
    m_gradient = - (2/n) * np.sum(x * (y - (m_now * x + b_now)))
    b_gradient = - (2/n) * np.sum(y - (m_now * x + b_now))

    gradient = np.sqrt(m_gradient**2 + b_gradient**2)

    return gradient

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

def train(points, m=0, b=0, L=0.0001, epsilon=0.00001, line_plot=None, error_plot=None):
    x_mean = points['km'].mean()
    x_std = points['km'].std()
    y_mean = points['price'].mean()
    y_std = points['price'].std()
    
    km_normalized, price_normalized = normalize(x_mean, x_std, y_mean, y_std, points)
    
    i = 0
    while (compute_gradient(km_normalized, price_normalized, m, b) > epsilon):
        m, b = gradient_descent(m, b, km_normalized, price_normalized, L)
        if i % 10 == 0:
            denormalize_m, denormalize_b = denormalize(x_mean, x_std, y_mean, y_std, m, b)
            update_line(points, denormalize_m, denormalize_b, line_plot)
            error = total_error(denormalize_m, denormalize_b, points['km'], points['price'])
            update_error_plot(i, error, error_plot)

        i += 1

    m_original, b_original = denormalize(x_mean, x_std, y_mean, y_std, m, b)
    return (m_original, b_original)

def update_data(data, m, b):
    df = pd.read_csv('lib/line_data.csv')
    df.loc[0, 'm'] = float(m)
    df.loc[0, 'b'] = float(b)
    df.to_csv('lib/line_data.csv', index=False)

#------------------ PLOT ------------------#

def on_click(event, data, m, b, line_plot, error_plot, button):
    print('Training...')
    new_m, new_b = train(data, m, b, L=0.01, epsilon=0.0001, line_plot=line_plot, error_plot=error_plot)
    update_data(data, new_m, new_b)
    print(f"y = {new_m.round(3)}x + {new_b.round(3)}")
    button.set_active(False)

def create_plot(data, m, b):
    x = data['km']
    y = data['price']

    plt.ion()  # Activar modo interactivo

    # Configuración de la figura para la regresión
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Gráfico de la regresión lineal
    ax1.scatter(x, y, label='Data points', color='blue')
    ax1.set_xlabel('Km')
    ax1.set_ylabel('Price')
    ax1.set_title('Price of a car according to its km')
    y_line = m * x + b
    line_plot, = ax1.plot(x, y_line, label=f'y = {m}x + {b}', color='red')
    ax1.legend()

    # Gráfico del error
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Error')
    ax2.set_title('Error according to the iterations')
    error_plot, = ax2.plot([], [], label='Total Error', color='green')
    ax2.legend()

    # Botón para entrenar
    ax_button = plt.axes([0.8, 0.05, 0.15, 0.075])
    button = Button(ax_button, 'Train')
    button.on_clicked(lambda event: on_click(event, data, m, b, line_plot, error_plot, button))

    plt.subplots_adjust(bottom=0.2)
    plt.subplots_adjust(hspace=0.5)  # Ajusta el espacio entre los subgráficos
    plt.show(block=True)  # Esto asegura que la ventana de matplotlib no se cierre automáticamente

    return (line_plot, error_plot)

def update_line(data, m, b, line_plot):
    x = data['km']
    y_line = m * x + b
    line_plot.set_ydata(y_line)
    line_plot.set_label(f"y = {m:.3f}x + {b:.3f}")
    line_plot.axes.legend()
    plt.draw()
    plt.pause(0.1)
    return line_plot


def update_error_plot(iteration, error, error_plot):
    # Obtener los datos actuales del gráfico
    x_data = np.append(error_plot.get_xdata(), iteration)
    y_data = np.append(error_plot.get_ydata(), error)
    
    # Actualizar los datos del gráfico
    error_plot.set_xdata(x_data)
    error_plot.set_ydata(y_data)

    # Recalcular y actualizar los límites de los ejes
    ax = error_plot.axes
    ax.relim()  # Recalcula los límites según los nuevos datos
    ax.autoscale_view()  # Ajusta la vista de los ejes automáticamente

    # Redibujar el gráfico
    plt.draw()
    plt.pause(0.1)



if __name__ == "__main__":
    data = pd.read_csv('lib/data.csv')
    m = 0
    b = 0

    line_plot, error_plot = create_plot(data, m, b)

