

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

# Transform and merge modules and programs
transformed_courses = []
for name, courses_with_same_name in grouped_courses.items():
    merged_modules = list(set([module for course in courses_with_same_name for module in course['modules']]))
    merged_programs = list(set([program for course in courses_with_same_name for program in course['programs']]))
    transformed_course = {
        "name": name,
        "modules": merged_modules,
        "programs": merged_programs
        # Add other fields as needed
    }
    transformed_courses.append(transformed_course)

# Write transformed data to a new JSON file without escaping non-ASCII characters
with open('transformed_data.json', 'w', encoding='utf-8') as f:
    json.dump(transformed_courses, f, indent=4, ensure_ascii=False)

print("Transformation complete. Transformed data written to 'transformed_data.json'.")
