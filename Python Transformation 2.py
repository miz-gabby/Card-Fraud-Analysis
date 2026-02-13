import pandas as pd
import json

# 1. Load the JSON file
with open('C:/Users/camar/Downloads/cleaned_Data.json', 'r') as f:
    data = json.load(f)

# 2. Extract the 'target' dictionary into a DataFrame
# list(data['target'].items()) gives us [(key, value), (key, value)]
df = pd.DataFrame(list(data['target'].items()), columns=['Attribute', 'Value'])

# 3. Remove spaces (strip) from both columns
# .astype(str) ensures we don't crash if a value is a number
df['Attribute'] = df['Attribute'].astype(str).str.strip()
df['Value'] = df['Value'].astype(str).str.strip()

# 4. Optional: Remove any resulting duplicates after stripping spaces
df = df.drop_duplicates()

# 5. Save to CSV
df.to_csv('cleaned_data22.csv', index=False)

print("Process complete: Spaces removed and CSV saved.")