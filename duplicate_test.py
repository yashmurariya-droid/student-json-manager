
import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

seen_names = set()

for student in students:
    name = student["name"].strip().lower()

    if name in seen_names:
        print("Duplicate found:", student["name"])
    else:
        seen_names.add(name)