# load data here
import pandas as pd

def load_data():
    df = pd.read_csv('dataset/housing.csv')
    df = clean_data(df)
    return df

def clean_data(df):
    df = df.fillna('')
    return df

df = load_data()
print(df.isna().sum())

