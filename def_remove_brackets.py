import pandas as pd

# Read the file into a DataFrame
df = pd.read_csv('excl-ADB 1952.txt', header=None, names=['text'])

# Use a regular expression to remove any text within parentheses, including the parentheses
df['text'] = df['text'].str.replace(r'\(.*?\)', '', regex=True)

# Save the cleaned DataFrame back to a file
df.to_csv('output.txt', index=False, header=False)
