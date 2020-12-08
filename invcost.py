import pandas as pd

df = pd.read_csv("inventory.csv")
df_quant = df['quant']
df_price = df['price']
cost = 0

for idx in range(len(df_quant)):
    cost += df_quant[idx] * df_price[idx]

print("Price: {}".format(cost))
