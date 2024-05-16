import json

# Read data from the JSON file
with open('courses-catalogue.courses7.0.json', 'r', encoding='utf-8') as f:
    previous_data = json.load(f)

# Group courses by name
grouped_courses = {}
for course in previous_data:
    name = course['name']
    if name not in grouped_courses:
        grouped_courses[name] = []
    grouped_courses[name].append(course)

# Transform and merge courses
transformed_courses = []
for name, courses_with_same_name in grouped_courses.items():
    merged_modules = list(set([module for course in courses_with_same_name for module in course['modules']]))
    merged_programs = list(set([program for course in courses_with_same_name for program in course['programs']]))

    # Example of selecting one of the values from the duplicates
    first_course = courses_with_same_name[0]  # Takes values from the first course instance

    transformed_course = {
        "course_id": first_course['course_id'],
        "name": name,
        "level_of_study": first_course['level_of_study'],
        "programs": merged_programs,
        "modules": merged_modules,
        "semester": first_course['semester'],
        "departments": first_course['departments'],
        "year_of_study": first_course['year_of_study'],
        "espb": first_course['espb'],
        "literature": first_course['literature'],
        "link": first_course['link'],
        "video": first_course['video'],
        "description": first_course['description'],
        "note": first_course['note'],
        "tags": first_course['tags'],
        "status": first_course['status'],
        "lecturers": first_course['lecturers']
    }
    transformed_courses.append(transformed_course)

# Write transformed data to a new JSON file without escaping non-ASCII characters
with open('transformed_data.json', 'w', encoding='utf-8') as f:
    json.dump(transformed_courses, f, indent=4, ensure_ascii=False)

print("Transformation complete. Transformed data written to 'transformed_data.json'.")
