import json
import re

def clean_magnitude(magnitude_str):
    """Extracts and returns the numeric part of the magnitude string."""
    # Remove the "Mag." prefix and any leading/trailing whitespace
    magnitude_str = magnitude_str.replace('Mag.', '').strip()
    
    # Remove any leading '+' sign
    magnitude_str = magnitude_str.lstrip('+').strip()
    
    # Find all numeric parts in the magnitude string
    magnitude_match = re.search(r'([\d.]+)', magnitude_str)
    if magnitude_match:
        try:
            # Convert the matched number to float and return
            return float(magnitude_match.group(1))
        except ValueError:
            # If conversion fails, return None
            return None
    else:
        # If no numeric part is found, return None
        return None

# Load the existing JSON data
with open('master_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Process each entry to convert the magnitude to a number
for entry in data:
    if 'magnitude' in entry:
        entry['magnitude'] = clean_magnitude(entry['magnitude'])

# Save the updated data to the JSON file
with open('extracted_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Magnitude values updated and saved to 'extracted_data.json'")
