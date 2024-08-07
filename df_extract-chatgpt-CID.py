import pandas as pd

# Read keywords from keywords.txt
with open('keywords.txt', 'r') as file:
    keywords = [line.strip() for line in file]

# Read lookup.txt into a DataFrame
lookup_df = pd.read_csv('lookup.txt', header=None, sep='\t')

# Create a DataFrame to store the results
results = []

# Iterate through keywords and search for matches in the first column of lookup.txt
for keyword in keywords:
    matched_lines = lookup_df[lookup_df[0].str.contains(keyword, na=False, regex=False)]
    if not matched_lines.empty:
        matched_lines['keyword'] = keyword
        results.append(matched_lines)

# Concatenate all matched lines into a single DataFrame
if results:
    results_df = pd.concat(results)
else:
    results_df = pd.DataFrame(columns=list(lookup_df.columns) + ['keyword'])

# Save the results to outlines.txt, ensuring tab-separated format is preserved
results_df.to_csv('outlines.txt', index=False, sep='\t', header=True)

print("Matching lines have been extracted and saved to outlines.txt")
