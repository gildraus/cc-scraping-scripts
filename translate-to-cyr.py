import pandas as pd
from transliterate import translit

# Load the Excel file
file_path = 'input/Prva_godina.xlsx'  # Update this path to your actual file path
df = pd.read_excel(file_path)

# Define a function to transliterate text to Cyrillic and trim spaces
def transliterate_and_trim(text):
    if isinstance(text, str):
        text = text.strip()  # Trim leading and trailing spaces
        text = translit(text, 'sr', reversed=False)  # Transliterate to Cyrillic
    return text

# Apply the function to each cell in the dataframe
for column in df.columns:
    df[column] = df[column].apply(transliterate_and_trim)

# Save the modified dataframe back to an Excel file
output_path = 'input/Prva_godina_cyrillic.xlsx'
df.to_excel(output_path, index=False)
