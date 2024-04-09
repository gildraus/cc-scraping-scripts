import json
import os

# Učitavanje JSON datoteke
with open('input-kursevi.json', 'r', encoding='utf-8') as file:
    courses = json.load(file)

# Funkcija za formatiranje knjige
def format_book(book):
    # Razdvajanje autora i ostalih informacija
    parts = book.split('.')
    author_info = parts[0].strip()
    book_info = '.'.join(parts[1:]).strip()
    # Dodavanje tačke nakon imena autora ako je nema
    if not author_info.endswith('.'):
        author_info += '.'
    # Vraćanje formatirane knjige
    return f"{author_info} {book_info}"

# Iteriranje kroz sve kurseve
for course in courses:
    # Ako je atribut "literature" string, pretvori ga u listu stringova
    if isinstance(course.get('literature'), str):
        literature_string = course['literature']
        # Razdvajanje stringa literature na osnovu zareza, uzimajući u obzir da je zarez i tačka separator
        literature_list = literature_string.split(',')
        # Formatiranje svake knjige u listi literature
        formatted_literature = [format_book(book) for book in literature_list]
        # Dodavanje formatirane literature u kurs
        course['literature'] = formatted_literature

# Provjera i kreiranje direktorijuma ako ne postoji
output_directory = 'output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Čuvanje izmijenjenih podataka u novoj datoteci
output_file = os.path.join(output_directory, 'novi_kursevi.json')
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(courses, file, ensure_ascii=False, indent=4)

print(f"Novi dokument sa izmijenjenim kursevima je sačuvan u '{output_file}'.")
