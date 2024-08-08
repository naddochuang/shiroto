import pandas as pd
import pubchempy as pcp

# Read the list of compounds from A.txt
compounds_file = 'trial-DEA.txt'
compounds = pd.read_csv(compounds_file, header=None, names=['Compound'])

# Function to get PubChem CID
def get_pubchem_cid(compound_name):
    try:
        result = pcp.get_compounds(compound_name, 'name')
        if result:
            return result[0].cid
        else:
            return None
    except Exception as e:
        return None

# Apply the function to get CIDs
compounds['PubChem CID'] = compounds['Compound'].apply(get_pubchem_cid)

# Print the resulting DataFrame
print(compounds)

# Optionally, save the results to a new CSV file
output_file = 'compounds_with_cids.csv'
compounds.to_csv(output_file, index=False)
