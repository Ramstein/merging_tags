
import pandas as pd

df = pd.read_csv("data.csv")

df1 = pd.read_csv("data2.csv")

df3 = pd.DataFrame()

for i, Id in enumerate(df['ID']):
    if i==0:
        df3 = df.iloc[i]
    else:
        if Id == df['ID'][i-1]:
            pd.concat([df3, df.iloc[i]], axis=1)

print(df, df1, df3)

# df3 = pd.merge(df, df1, how='outer')

df3.to_csv("df3.csv", index=False)

# print(df3.columns.tolist())
print(df3)