#!/bin/bash

input_file="input_data-3598.txt"  # Replace with your input file path
output_file="output_data-3598-tab.txt"  # Replace with your desired output file path

# Define the column headers
headers="##TITLE\t##JCAMPDX\t##DATA TYPE\t##SAMPLE DESCRIPTION\t##CAS NAME\t##NAMES\t##MOLFORM\t##CAS REGISTRY NO\t##MP\t##BP\t##MW\t##$RETENTION INDEX\t##$CONDENSED SPECTRUM\t##NPOINTS"

# Initialize the output file with headers
echo -e "$headers" > "$output_file"

# Initialize variables
inside_xydata=false
record=""

# Read the input file line by line
while IFS= read -r line; do
    # Check for the start of XYDATA
    if [[ "$line" == "##XYDATA=(XY..XY)" ]]; then
        inside_xydata=true
        continue
    fi

    # Check for the end of the record
    if [[ "$line" == "##END=" ]]; then
        inside_xydata=false
        # Append the record to the output file
        echo -e "$record" >> "$output_file"
        record=""
        continue
    fi

    # Skip lines inside XYDATA section
    if $inside_xydata; then
        continue
    fi

    # Extract key-value pairs and append to the record
    if [[ "$line" == "##"* ]]; then
        key=$(echo "$line" | cut -d'=' -f1)
        value=$(echo "$line" | cut -d'=' -f2-)
        record+="$value\t"
    fi
done < "$input_file"

echo "Data has been saved to $output_file"
