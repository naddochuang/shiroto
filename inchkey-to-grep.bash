#!/bin/bash

inchikeys_file="inchkey-no-CAS.txt"  # File containing the list of InChIKeys
data_file="output_data-3598-tab.txt"            # File containing the data to search
output_file="output-inchkey-to-CAS.txt"        # File to save the grep results

# Clear the output file if it exists
> "$output_file"

# Read each InChIKey from the inchikeys file
while IFS= read -r inchikey; do
    # Use grep to find lines containing the InChIKey and append to the output file
    grep "$inchikey" "$data_file" >> "$output_file"
done < "$inchikeys_file"

echo "Data has been saved to $output_file"
