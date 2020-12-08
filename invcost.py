import pandas as pd

df = pd.read_csv("inventory.csv")
print("Price: {}".format(sum(df['price'])))