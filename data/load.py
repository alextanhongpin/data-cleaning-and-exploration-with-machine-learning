import pandas as pd


def load_covid():
    df = pd.read_csv('./data/covidtotals.csv')
    df.set_index('iso_code', inplace=True)
    return df


def load_nls97():
    """loads the National Longitudinal Survey dataset"""
    df = pd.read_csv("./data/nls97.csv")
    df.set_index('personid', inplace=True)
    return df

def load_nls97b():
    """loads the National Longitudinal Survey dataset"""
    df = pd.read_csv("./data/nls97b.csv")
    df.set_index('personid', inplace=True)
    return df