
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
    else:
        print("Would remove duplicate:", student["name"])

print("\nPreview of cleaned records:")
for student in cleaned_students:
    print(student["name"], "-", student["marks"])

print("\nOriginal records:", len(students))
print("Records after cleanup:", len(cleaned_students))