
import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

cleaned_students = []
seen_names = set()

for student in students:
    name = student["name"].strip().lower()

    if name not in seen_names:
        seen_names.add(name)
        cleaned_students.append(student)

with open("students_cleaned.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_students, file, indent=4)

print("Cleaned data saved successfully!")
print("Original records:", len(students))
print("Cleaned records:", len(cleaned_students))