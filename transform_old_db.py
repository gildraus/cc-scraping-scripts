import json

# Učitavanje podataka iz JSON datoteke
with open("courses6.json", "r", encoding="utf-8") as file:
    json_data = file.read()

# Pretvaranje JSON stringa u Python listu objekata
courses = json.loads(json_data)

# Nova lista za transformisane podatke
transformed_courses = []

# Iteriranje kroz svaki kurs
for course in courses:
    # Kreiranje novog kursa sa željenim atributima
    new_course = {
        "course_id": course.get("course_id", ""),
        "name": course.get("name", ""),
        "level_of_study": course.get("level_of_study", ""),
        "programs": [course.get("program", "")],  # Dodavanje trenutnog programa kao prve stavke u listu
        "modules": course.get("modules", []),
        "semester": course.get("semester", ""),
        "departments": course.get("departments", []),
        "year_of_study": course.get("year_of_study", ""),
        "espb": course.get("espb", ""),
        "literature": course.get("literature", []),
        "link": course.get("link", ""),
        "video": course.get("video", ""),
        "description": course.get("description", ""),
        "note": course.get("note", ""),
        "tags": course.get("tags", []),
        "status": course.get("status", ""),
        "lecturers": course.get("lecturers", [])
    }

    # Dodavanje transformisanog kursa u novu listu
    transformed_courses.append(new_course)

# Upisivanje transformisanih podataka u novu JSON datoteku
with open("courses.json", "w", encoding="utf-8") as file:
    json.dump(transformed_courses, file, indent=2, ensure_ascii=False)

print("Podaci su uspešno upisani u courses.json.")
