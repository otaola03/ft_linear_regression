import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

# Función para calcular el precio basado en la regresión lineal
def predict_price(km, m, b):
    return m * km + b

# Función para crear la gráfica
def create_plot(data, m, b):
    x = data.iloc[:, 0]  # Primera columna (km) como eje X
    y = data.iloc[:, 1]  # Segunda columna (price) como eje Y

    # Dibujar los puntos de datos
    plt.scatter(x, y, label='Data points', color='blue')

    # Etiquetas y título
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Price of a car according to its km')

    # Crear la línea de ajuste
    y_line = m * x + b  # Ecuación de la línea
    line_plot, = plt.plot(x, y_line, label=f'y = {m:.2f}x + {b:.2f}', color='red')

    # Mostrar la leyenda
    plt.legend()

    # Retornar el objeto de la línea para posibles actualizaciones
    return line_plot

# Función para manejar el clic en el botón y calcular el precio
def on_button_click(event):
    try:
        km_input = float(text_box.text)  # Obtener valor ingresado
        price = predict_price(km_input, m, b)  # Calcular precio
        print(f"Input km: {km_input}, Predicted price: {price}")
        
        # Dibujar el punto en la gráfica
        point_plot.set_offsets([km_input, price])  # Actualizar posición del punto
        plt.draw()  # Actualizar la gráfica
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    data = pd.read_csv("lib/data.csv")
    m, b = pd.read_csv("lib/line_data.csv").values[0]
    
    # Crear la figura
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.subplots_adjust(bottom=0.2)  # Ajustar espacio para botones

    # Crear la gráfica con la línea de regresión
    line_plot = create_plot(data, m, b)

    # Crear un marcador para el punto del valor ingresado
    point_plot = ax.scatter([], [], color='green', label='Predicted point', zorder=5)
    plt.legend()

    # Crear input para el valor de km
    ax_box = plt.axes([0.2, 0.05, 0.5, 0.075])  # Posición del TextBox
    text_box = TextBox(ax_box, "Enter km: ")

    # Crear botón para calcular
    ax_button = plt.axes([0.75, 0.05, 0.15, 0.075])  # Posición del botón
    button = Button(ax_button, "Predict")
    button.on_clicked(on_button_click)  # Asignar evento al botón

    # Mostrar la gráfica
    plt.show()

