import pandas as pd
from train import train

def get_data(data):
    return pd.read_csv(data)

if __name__ == "__main__":
    data = get_data('lib/data.csv')
    train(data)

