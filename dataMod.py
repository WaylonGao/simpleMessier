import json
import re

# Load the existing JSON data
with open('master_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Process each entry to convert the magnitude to a number
for entry in data:
    if 'magnitude' in entry:
        # Extract the numeric part of the magnitude
        magnitude_match = re.search(r'([\d.]+)', entry['magnitude'])
        if magnitude_match:
            entry['magnitude'] = float(magnitude_match.group(1))
        else:
            # Handle cases where magnitude is not in the expected format
            entry['magnitude'] = None

# Save the updated data to the JSON file
with open('extracted_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Magnitude values updated and saved to 'extracted_data.json'")
