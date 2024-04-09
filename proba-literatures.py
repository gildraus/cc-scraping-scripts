import json
import os

# Funkcija za formatiranje knjige
def format_book(book):
    parts = book.split('. ')  # Razdvajanje knjige na osnovu tačke i razmaka
    formatted_parts = []

    # Iteriranje kroz delove knjige i formatiranje
    for part in parts:
        # Dodavanje tačke nakon imena autora ako je potrebno
        if part.endswith(',') or part.strip().isdigit():
            formatted_parts[-1] += f'. {part.strip()}'
        else:
            formatted_parts.append(part.strip())

    return ' '.join(formatted_parts)

# Učitavanje JSON datoteke
input_file = 'input-kursevi.json'
output_file = 'output-kursevi.json'

with open(input_file, 'r', encoding='utf-8') as file:
    courses = json.load(file)

# Iteriranje kroz sve kurseve
for course in courses:
    # Ako je atribut "literature" string, pretvori ga u listu stringova
    if isinstance(course.get('literature'), str):
        literature_string = course['literature']
        # Razdvajanje stringa literature na osnovu zareza
        literature_list = literature_string.split(', ')
        # Formatiranje svake knjige u listi literature
        formatted_literature = [format_book(book) for book in literature_list]
        # Dodavanje formatirane literature u kurs
        course['literatures'] = formatted_literature

# Čuvanje izmijenjenih podataka u novoj datoteci
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(courses, file, ensure_ascii=False, indent=4)

print(f"Novi dokument sa izmijenjenim kursevima je sačuvan u '{output_file}'.")
