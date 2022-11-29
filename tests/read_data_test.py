import pandas as pd

from config import *

def read_data_test():
    df = pd.read_csv(DATA_PATH + "/" + DATA_NAME, nrows=N_ROWS)
    print(df.head())

if __name__ == "__main__":
    read_data_test()