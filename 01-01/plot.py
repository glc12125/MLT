"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    df['High'].plot()
    plt.show()  # must be called to show plots

def test_run2():
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    df[['Close', 'Adj Close']].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
