import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"amazon.csv")

df=df.dropna(subset=['product_name','user_id','review_id'])
