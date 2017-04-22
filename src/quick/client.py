import src.quick.panda as qpn

# импортируем Pandas и Numpy
import pandas as pd
import numpy as np


def main():
    df = pd.read_csv('data/test.csv')
    qpn.show_table(df, 1)
