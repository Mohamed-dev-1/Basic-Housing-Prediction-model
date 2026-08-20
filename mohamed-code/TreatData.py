# load data here
import pandas as pd

def load_data():
    df = pd.read_csv('dataset/housing.csv')
    df = clean_data(df)
    return df

def clean_data(df):
    
    # data already clean from duplicates
    # we found empty cells only in total_bedrooms column so i see that need to replace empty cells with the median value to ensure that the dtype stays float64 and not become an ibject when try to fill them with '' empty strings
    df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())
    
    # replace the ocean_proximity column with 5 -> set(values in this columns) columns each column 
    df = pd.get_dummies(df, columns=['ocean_proximity'])
    
    # no need to clean data from wrong format or data it looks good
    return df



