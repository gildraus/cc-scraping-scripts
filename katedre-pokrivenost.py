import json

# Učitavanje prvog dokumenta
with open('pokrivenostNastave.json', 'r', encoding='utf-8') as file1:
    dokument1 = json.load(file1)

# Učitavanje drugog dokumenta
with open('katedre.json', 'r', encoding='utf-8') as file2:
    dokument2 = json.load(file2)

# Spajanje dokumenata na osnovu course_id
for kurs1 in dokument1:
    for kurs2 in dokument2:
        if kurs1['course_id'] == kurs2['course_id']:
            kurs1['departments'] = kurs2['departments']
            # Dodavanje atributa level_of_study
            kurs1['level_of_study'] = "Мастер академске студије"
            break  # Prekidamo petlju kada pronađemo odgovarajući kurs

# Čuvanje spojenog dokumenta u novi JSON fajl
with open('spojeni_dokument.json', 'w', encoding='utf-8') as output_file:
    json.dump(dokument1, output_file, ensure_ascii=False, indent=4)
