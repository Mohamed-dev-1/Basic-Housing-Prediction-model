# main code here

from TreatData import load_data
from model import model_predict

df = load_data()

pred = model_predict(df)

print(pred)
