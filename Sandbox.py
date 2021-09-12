import pandas as pd

pop = pd.read_csv("PEB07.20210911T110934.csv")

df=pd.DataFrame(pop)
print(df.head())
print(df.info())

df.astype({"VALUE": str}).dtypes #Why does this not work?
print(df.info())












