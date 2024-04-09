import pandas as pd
import json

# Učitavanje Excel tabele
df = pd.read_excel('pokrivenostNastave.xlsx')

# Odabir potrebnih kolona i preimenovanje kolona
df = df[['Шифра', 'Предмет', 'Модул', 'Координатор предмета', 'Предавања', 'Вежбе']]
df.columns = ['course_id', 'name', 'modules', 'coordinator', 'lectures', 'exercises']

# Filtriranje redova sa nedostajućim vrednostima course_id ili imenima
df = df.dropna(subset=['course_id', 'name'])

# Razdvajanje modula i predavača koji su odvojeni zarezom, uz proveru da li je vrednost string pre razdvajanja
df['modules'] = df['modules'].apply(lambda x: [module.strip() for module in str(x).split(',') if module.strip()])
df['lecturers'] = df.apply(lambda row: list(set([lecturer.strip() for lecturer in str(row['lectures']).split(',') if lecturer.strip()] + [lecturer.strip() for lecturer in str(row['exercises']).split(',') if lecturer.strip()])), axis=1)

# Odabir potrebnih kolona i pretvaranje u JSON format
result = df[['course_id', 'name', 'modules', 'lecturers']].to_dict(orient='records')

# Čuvanje rezultata u JSON fajl
with open('pokrivenostNastave.json', 'w') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)
