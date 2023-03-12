import pandas as pd


def load_covid():
    df = pd.read_csv('./data/covidtotals.csv')
    df.set_index('iso_code', inplace=True)
    return df