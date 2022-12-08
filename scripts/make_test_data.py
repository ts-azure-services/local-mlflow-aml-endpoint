import pandas as pd
import json
df = pd.read_csv("./data/ames_housing.csv")
feature_columns = ["Lot Area", "Gr Liv Area", "Garage Area", "Bldg Type"]
selected = df.loc[30:50, feature_columns]

existing_values = selected.to_json(orient="split")
filename = f'./data/test_data.json'

# Two styles of getting JSON output
# The second option takes out strings - which can sometimes cause an error at the endpoint
option_1 = True # default
#option_1 = False
option_2 = False

if option_1:
    new_dict = {'input_data': existing_values}
    # Write out test data
    with open(filename, 'w') as f:
        json.dump(new_dict, f)

if option_2:
    parsed = json.loads(existing_values)
    # Write out test data
    with open(filename, 'w') as f:
        f.write(json.dumps({'input_data':parsed}))
