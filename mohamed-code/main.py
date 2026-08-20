# main code here

from TreatData import load_data
from model import model_predict, score

df = load_data()

pred = model_predict(df)

print(f"model predections: {pred}")

