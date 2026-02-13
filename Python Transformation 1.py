import json

file_path = 'C:/Users/camar/OneDrive/Desktop/Financial Transactions Dataset/train_fraud_labels.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# If 'target' contains a list of dictionaries
if isinstance(data['target'], list):
    # This trick converts each dict to a string to make it "hashable", 
    # removes duplicates, then converts back to a dict.
    seen = set()
    unique_data = []
    for d in data['target']:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            unique_data.append(d)
    data['target'] = unique_data

# Save it back
with open('cleaned_Data.json', 'w') as f:
    json.dump(data, f, indent=4)