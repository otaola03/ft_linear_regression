import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

def predict_price(km, m, b):
    return m * km + b

def create_plot(data, m, b):
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]

    plt.scatter(x, y, label='Data points', color='blue')

    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Price of a car according to its km')

    y_line = m * x + b
    line_plot, = plt.plot(x, y_line, label=f'y = {m:.2f}x + {b:.2f}', color='red')

    plt.legend()

    return line_plot


def on_button_click(event):
    try:
        km_input = float(text_box.text)
        price = predict_price(km_input, m, b)
        print(f"Input km: {km_input}, Predicted price: {price}")
        
        point_plot.set_offsets([km_input, price])
        plt.draw()

    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")


if __name__ == "__main__":
    data = pd.read_csv("lib/data.csv")
    m, b = pd.read_csv("lib/line_data.csv").values[0]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.subplots_adjust(bottom=0.2)

    line_plot = create_plot(data, m, b)

    # Crear un marcador para el punto del valor ingresado
    point_plot = ax.scatter([], [], color='green', label='Predicted point', zorder=5)
    plt.legend()

    ax_box = plt.axes([0.2, 0.05, 0.5, 0.075])
    text_box = TextBox(ax_box, "Enter km: ")

    ax_button = plt.axes([0.75, 0.05, 0.15, 0.075])  # Posición del botón
    button = Button(ax_button, "Predict")
    button.on_clicked(on_button_click)  # Asignar evento al botón

    # Mostrar la gráfica
    plt.show()

