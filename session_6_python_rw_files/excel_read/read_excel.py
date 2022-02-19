import pandas as pd

path = './documento.xlsx'
df = pd.read_excel(path)
print("show df")
print(df)

df["new value"] = True

print("show describe")
print(df.describe())

df.to_excel("output.xlsx")
