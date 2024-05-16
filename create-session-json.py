import pandas as pd
import json

# Load the Excel file
file_path = 'input/Prva_godina_cyrillic.xlsx'  # Updated file path
df = pd.read_excel(file_path)


# Define a function to create the JSON structure
def create_json_structure(df):
    result = []

    # Iterate over each row in the dataframe
    for _, row in df.iterrows():
        subject_data = {
            "name": row['Назив'],
        }

        session_time = f"{row['Дан']} - {row['Термин']} {row['Место']} ({row['Група']})"

        if row['П/В'] == 'П':
            subject_data["lecture_session_time"] = session_time
        elif row['П/В'] == 'В':
            subject_data["exercise_session_time"] = session_time

        result.append(subject_data)

    return result


# Create the JSON structure
json_structure = create_json_structure(df)

# Save the JSON structure to a file
output_path = 'input/Prva_godina.json'  # Updated output path
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_structure, json_file, ensure_ascii=False, indent=4)

# Output path to the generated JSON file
print(f"JSON file generated at: {output_path}")
