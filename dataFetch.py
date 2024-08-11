import re
import json
from bs4 import BeautifulSoup

# Load the HTML file
with open('catalog.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Initialize an empty list to hold the extracted data
data = []

# Find all entries
entries = soup.find_all('h3', class_='wp-block-heading p1')

# Loop through each entry and extract the information
for entry in entries:
    entry_data = {}
    
    # Extract the name
    name_tag = entry.find_next('img')
    if name_tag:
        full_name = name_tag.get('title')
        # Filter out anything after "Credit:"
        name = re.split(r'\s*Credit:\s*', full_name)[0]
        entry_data['name'] = name
    
    # Extract the coordinates
    coord_tag = entry.find_next('li', text=re.compile(r'^RA'))
    if coord_tag:
        entry_data['coordinates'] = coord_tag.text
    
    # Extract the magnitude
    mag_tag = entry.find_next('li', text=re.compile(r'^Mag'))
    if mag_tag:
        entry_data['magnitude'] = mag_tag.text
    
    # Add the entry data to the list
    data.append(entry_data)

# Save the data to a JSON file
with open('extracted_data1.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Data extracted and saved to 'extracted_data.json'")
