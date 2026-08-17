# main code here

from TreatData import load_data

df = load_data()

# separate between features and target
features = df.drop(['median_house_value'])

# 
target = df['median_house_value']