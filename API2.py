import requests

# Define the PUG-REST URL base
pugrest_prolog = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"

# Read the input CSV file
input_file = "209-ADB-trial2.csv"
with open(input_file, "r") as f:
    compound_names = [line.strip() for line in f]

# Ensure the "Compound Name" column exists (if using pandas)
# if you're using pandas to read the CSV, uncomment these lines:
import pandas as pd
df = pd.read_csv(input_file)
compound_names = df["Compound Name"].tolist()  # Assuming "Compound Name" is a column

# Loop through each compound name
for compound_name in compound_names:
    # Build the complete URL
    url = f"{pugrest_prolog}{compound_name}/cids/TXT"

    # Send the GET request and process the response
    response = requests.get(url)
    if response.status_code == 200:
        cids = response.text.strip().split()
        print(f"{compound_name} {cids}")
    else:
        print(f"Error fetching CIDs for {compound_name}: {response.status_code}")
