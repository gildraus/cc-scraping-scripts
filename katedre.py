import pandas as pd
import json

# Učitavanje Excel tabele
excel_file = 'MAS Predmet - Katedre.xlsx'  # Naziv Excel fajla
sheet_name = 'Sheet1'  # Naziv radnog lista
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Pretvaranje DataFrame-a u listu kurseva
courses = []
for index, row in df.iterrows():
    course_id = str(row['Шифра предмета'])
    name = str(row['Назив предмета'])
    departments = str(row['Катедра'])
    course = {
        'course_id': course_id,
        'name': name,
        'departments': departments
    }
    courses.append(course)

# Konvertovanje u JSON format
json_data = json.dumps(courses, ensure_ascii=False, indent=4)

# Ispis JSON-a
print(json_data)

# Čuvanje JSON-a u fajl
with open('katedre.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
