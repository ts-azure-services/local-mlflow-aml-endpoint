import pandas as pd
import json
df = pd.read_csv("./data/ames_housing.csv")
feature_columns = ["Lot Area", "Gr Liv Area", "Garage Area", "Bldg Type"]
cat_features = ["Bldg Type"]
selected = df.loc[30:200, feature_columns]
#temp = selected.copy()

## Split building type col into one hot encoded cols
#for col in list(selected.columns):
#    if col in cat_features:
#        # One-hot encoding
#        dummies = pd.get_dummies(temp[col])
#        # Drop the original column
#        final = pd.concat([selected.drop([col], axis=1), dummies], axis=1)
#
#assert len(final.columns) == 8
#print(f"Sample data:\n{final.head()}")

# Split into JSON representation
existing_values = selected.to_json(orient="split")
option_1 = True # default
option_2 = True

# Two styles of getting JSON output
if option_1:
    new_dict = {'input_data': existing_values}
    # Write out test data
    filename = f'./data/test_data_option1.json'
    with open(filename, 'w') as f:
        json.dump(new_dict, f)

# The second option takes out strings - which can sometimes cause an error at the endpoint
# especially when signatures have been inferred
if option_2:
    parsed = json.loads(existing_values)
    # Write out test data
    filename = f'./data/test_data_option2.json'
    with open(filename, 'w') as f:
        f.write(json.dumps({'input_data':parsed}))
