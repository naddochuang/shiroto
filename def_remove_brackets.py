import pandas as pd

# Read the file into a DataFrame
df = pd.read_csv('excl-ADB 1952.txt', header=None, names=['text'])

# Use a regular expression to remove any text within parentheses, including the parentheses
df['text'] = df['text'].str.replace(r'\(.*?\)', '', regex=True)

# 1. Replace two spaces with one space
df['text'] = df['text'].str.replace('  ', ' ')

# 2. Trim any leading and trailing spaces
df['text'] = df['text'].str.strip()

# Save the cleaned DataFrame back to a file
df.to_csv('output.txt', index=False, header=False)
