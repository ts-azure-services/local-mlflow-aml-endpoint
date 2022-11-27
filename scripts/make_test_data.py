import pandas as pd
import json
df = pd.read_csv("./data/ames_housing.csv")
feature_columns = ["Lot Area", "Gr Liv Area", "Garage Area", "Bldg Type"]
selected = df.loc[30:50, feature_columns]
existing_values = selected.to_json(orient="split")
new_dict = {'input_data': existing_values}
filename = f'./data/test_data.json'

# Write out test data
with open(filename, 'w') as f:
    json.dump(new_dict, f)
