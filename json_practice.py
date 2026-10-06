
import json
import os

filename = "students_cleaned.json"


def load_students():
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, list):
                return data

            print("Invalid student data format. Starting with an empty list.")

        except (json.JSONDecodeError, OSError) as error:
            print("Could not read student data:", error)

    return []


def save_students(students):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def valid_student(student):
    return (
        isinstance(student, dict)
        and isinstance(student.get("name"), str)
    )


def find_student(students, name):
    for student in students:
        if (
            valid_student(student)
            and student["name"].strip().lower() == name.strip().lower()
        ):
            return student

    return None


def add_student(students):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if find_student(students, name) is not None:
        print(f"Student '{name}' already exists!")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter marks as a number.")
        return

    new_student = {"name": name, "marks": marks}
    students.append(new_student)

    try:
        save_students(students)
        print("Student saved successfully!")

    except OSError as error:
        students.pop()
        print("File operation failed:", error)


def search_student(students):
    name = input("Enter name to search: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    student = find_student(students, name)

    if student is not None:
        print("\nStudent found!")
        print("Name:", student["name"])
        print("Marks:", student.get("marks", "Not available"))
    else:
        print("Student not found.")


def update_marks(students):
    name = input("Enter student name to update: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    student = find_student(students, name)

    if student is None:
        print("Student not found.")
        return

    print(
        f"Found: {student['name']} - "
        f"Current marks: {student.get('marks', 'N/A')}"
    )

    try:
        new_marks = float(input("Enter new marks (0-100): "))

        if not 0 <= new_marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter marks as a number.")
        return

    had_marks = "marks" in student
    old_marks = student.get("marks")
    student["marks"] = new_marks

    try:
        save_students(students)
        print(f"Updated {student['name']}'s marks to {new_marks}!")

    except OSError as error:
        if had_marks:
            student["marks"] = old_marks
        else:
            student.pop("marks", None)

        print("File operation failed:", error)


def delete_student(students):
    name = input("Enter student name to delete: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    student = find_student(students, name)

    if student is None:
        print("Student not found.")
        return

    print(
        f"Found: {student['name']} - "
        f"Marks: {student.get('marks', 'N/A')}"
    )

    confirm = input(
        f"Are you sure you want to delete "
        f"'{student['name']}'? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    index = students.index(student)
    deleted_student = students.pop(index)

    try:
        save_students(students)
        print(f"Deleted {deleted_student['name']} successfully!")

    except OSError as error:
        students.insert(index, deleted_student)
        print("File operation failed:", error)


def show_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- All Students ---")

    for student in students:
        if valid_student(student):
            print(
                student["name"],
                "-",
                student.get("marks", "N/A")
            )
        else:
            print("Invalid student record:", student)

    valid_marks = [
        student["marks"]
        for student in students
        if valid_student(student)
        and isinstance(student.get("marks"), (int, float))
        and not isinstance(student.get("marks"), bool)
        and 0 <= student["marks"] <= 100
    ]

    print("Total records:", len(students))

    if valid_marks:
        average = sum(valid_marks) / len(valid_marks)
        print("Average marks:", round(average, 2))
    else:
        print("No valid marks available for calculating average.")


def main():
    students = load_students()

    while True:
        print("\n=== Student JSON Manager ===")
        print("1. Add student")
        print("2. Search student")
        print("3. Update marks")
        print("4. Delete student")
        print("5. Show all students")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            update_marks(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            show_students(students)

        elif choice == "6":
            print("Goodbye, Yash!")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()