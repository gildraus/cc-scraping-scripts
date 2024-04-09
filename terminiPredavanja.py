import pandas as pd
import json

# Učitavanje Excel datoteke
df = pd.read_excel('terminiPredavanja.xlsx')

# Mapiranje kolona
column_mapping = {
    'Шифра': 'course_id',
    'Датум': 'datum',
    'Време': 'vreme',
    'Сала': 'sala'
}

# Pretvaranje podataka u JSON format
courses = []
for index, row in df.iterrows():
    course = {}
    for excel_col, json_col in column_mapping.items():
        if pd.notna(row[excel_col]):
            if json_col not in course:
                course[json_col] = []
            course[json_col].append(str(row[excel_col]))
    # Sastavljanje atributa lecture_session_times
    if 'datum' in course and 'vreme' in course and 'sala' in course:
        lecture_sessions = [f"{v} - {s}" for v, s in zip(course['vreme'], course['sala'])]
        course['lecture_session_times'] = ', '.join(lecture_sessions)
        # Uklanjanje pojedinačnih atributa
        del course['datum']
        del course['vreme']
        del course['sala']
    courses.append(course)

# Pisanje u JSON datoteku
with open('kursevi.json', 'w', encoding='utf-8') as json_file:
    json.dump(courses, json_file, ensure_ascii=False, indent=4)
