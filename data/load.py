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

def load_nls97compba():
    """loads the National Longitudinal Survey dataset"""
    df = pd.read_csv("./data/nls97compba.csv")
    df.set_index('personid', inplace=True)
    return df


def load_nls97wages():
    """loads the National Longitudinal Survey dataset"""
    df = pd.read_csv("./data/nls97wages.csv")
    return df


def load_nls97degreelevel():
    """loads the National Longitudinal Survey dataset"""
    df = pd.read_csv("./data/nls97degreelevel.csv")
    return df


def load_ltpoland():
    """loads the land temperature from Poland"""
    df = pd.read_csv("./data/ltpoland.csv")
    df.set_index('station', inplace=True)
    df.dropna(inplace=True)
    return df


def load_landtemps2019avgs():
    """The land temperature datase contains the average temperature readings 
    (in Celsius) in 2019 from over 12,000 stations across the world."""
    df = pd.read_csv("./data/landtemps2019avgs.csv")
    return df


def load_fossilfueltaxrate14():
    """This dataset on implied gasoline tax by country is available for 
    public use on the Harvard Dataverse.
    """
    df = pd.read_csv("./data/fossilfueltaxrate14.csv")
    df.set_index('countrycode', inplace=True)
    return df


def load_un_income():
    df = pd.read_csv("./data/un_income_gap.csv")
    df.set_index('country', inplace=True)
    df['incomeratio'] = df.femaleincomepercapita / df.maleincomepercapita
    df['educratio'] = df.femaleyearseducation / df.maleyearseducation
    df['laborforcepartratio'] = df.femalelaborforceparticipation / df.malelaborforceparticipation
    df['humandevratio'] = df.femalehumandevelopment / df.malehumandevelopment
    df.dropna(subset=['incomeratio'], inplace=True)
    
    return df
    