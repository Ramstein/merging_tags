import pandas as pd


def set_dataframe(df, index):
    df.at[index, 'Name'] = row['Name']
    df.at[index, 'region'] = row['region']
    df.at[index, 'ID'] = row['ID']
    df.at[index, 'Type'] = row['Type']
    df.at[index, 'TagKey'] = row['TagKey']
    df.at[index, 'TagValue'] = row['TagValue']
    old_instance_id = row['ID']
    return df, old_instance_id


df_input = pd.read_csv("input_data.csv", index_col=None)
df_merged = pd.DataFrame(data={
    "Name": [],
    "region": [],
    "ID": [],
    "Type": [],
    "TagKey": [],
    "TagValue": []
})

old_instance_id = ''
old_instance_index = 0
old_instance_index_tag_value = 1

for index, row in df_input.iterrows():
    if index == 0:
        df_merged, old_instance_id = set_dataframe(df_merged, index)
        old_instance_index += 1

    elif old_instance_id == row['ID']:
        df_merged.at[old_instance_index - 1, f'TagKey{old_instance_index_tag_value}'] = row['TagKey']
        df_merged.at[old_instance_index - 1, f'TagValue{old_instance_index_tag_value}'] = row['TagValue']
        old_instance_index_tag_value += 1

    else:
        df_merged, old_instance_id = set_dataframe(df_merged, old_instance_index)
        old_instance_index += 1
        old_instance_index_tag_value = 1

df_merged.to_csv("output_merged_tags_keys_values.csv", index=False)
