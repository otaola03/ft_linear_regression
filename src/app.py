import pandas as pd
from train import train
import matplotlib.pyplot as plt

def get_data(data):
    return pd.read_csv(data)

if __name__ == "__main__":
    data = get_data('lib/data.csv')
    m, b = train(data)
    print(m, b)
