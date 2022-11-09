
import pandas as pd

df = pd.read_csv("data.csv", index_col=None)

df3 = pd.DataFrame(data={
    "Name": [],
    "region": [],
    "ID": [],
    "Type": [],
    "TagKey": [],
    "TagValue":[]
})
print(df3)

for i, Id in enumerate(df['ID']):
    if i==0:
        # df3 = pd.concat([df3, df.iloc[i].T], axis=1)
        df3 = df.iloc[i].T
        print(df3)
    elif Id == df['ID'][i-1]:
        df3[f"TagKey{i}"] = df.iloc[i]["TagKey"]
        df3[f"TagValue{i}"] = df.iloc[i]["TagValue"]
        # print(df.iloc[i])
        # df3 = pd.concat([df3, df.iloc[i].T], axis=1)
        # print(df3)
    else: 
        df3 = pd.concat([df3, df.iloc[i].T], axis=1)
        # df3[f"TagKey{i}"] = df.iloc[i]["TagKey"]
        # df3[f"TagValue{i}"] = df.iloc[i]["TagValue"]
# print(df, df3)

# df3 = pd.merge(df, df1, how='outer')

df3.to_csv("df3.csv", index=False)

# print(df3.columns.tolist())
# print(df3)