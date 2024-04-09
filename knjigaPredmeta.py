import PyPDF2
import re
import json


def extract_course_data(pdf_file):
    # Otvori PDF datoteku
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        data = {'courses': []}

        # Iteriraj kroz stranice PDF-a počevši od sedme stranice
        for page_num in range(6, num_pages):  # Počevši od indeksa 6 (što odgovara sedmoj stranici)
            page = reader.getPage(page_num)
            text = page.extractText()

            # Pronađi sve potrebne informacije koristeći regularne izraze
            matches = re.findall(
                r'Ознака предмета: (.+)\nБрој ЕСПБ: (\d+).+?Садржај/структура предмета:\n(.+?)\nЛитература\n(.*?)\d{2}.\d{2}.\d{4}',
                text, re.DOTALL)

            # Izdvoji podatke za svaki predmet
            for match in matches:
                course = {
                    'oznaka_predmeta': match[0],
                    'broj_espb': int(match[1]),
                    'sadrzaj_struktura_predmeta': match[2].strip(),
                    'literatura': match[3].strip().split('\n')
                }
                data['courses'].append(course)

    return data


# Pozovi funkciju za ekstrakciju podataka
course_data = extract_course_data('kp201ep.pdf')

# Ispiši podatke u konzolu
print(json.dumps(course_data, ensure_ascii=False, indent=4))
