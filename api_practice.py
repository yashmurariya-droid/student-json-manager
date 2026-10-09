import requests
import json

try:
    url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    todos = response.json()

    completed_todos = []

    for todo in todos:
        if todo["completed"] :
            completed_todos.append(todo)

    print("Total completed todos:", len(completed_todos))
    
    # Save the completed todos to a JSON file
    with open("completed_todos.json", "w") as file:
        json.dump(completed_todos, file, indent=4)
    
    print("Completed todos saved to completed_todos.json")
    
    print("\nFirst 5 completed todos:")

    for todo in completed_todos[:5]:
        print("ID:", todo["id"])
        print("Title:", todo["title"])
        print("-" * 30)
	 

        # Read the saved JSON file
    with open("completed_todos.json", "r") as file:
        saved_todos = json.load(file)

    print("\n--- Saved Data Verification ---")
    print("Records loaded:", len(saved_todos))
    print("First saved task:", saved_todos[0]["title"])
    
    # Count completed tasks for each user
    user_counts = {}

    for todo in saved_todos:
        user_id = todo["userId"]

        if user_id not in user_counts:
            user_counts[user_id] = 0

        user_counts[user_id] += 1

    print("\n--- Completed Tasks by User ---")

    for user_id, count in user_counts.items():
        print(f"User {user_id}: {count} completed tasks")
        # Save the summary report
    report = {
        "total_completed": len(saved_todos),
        "total_users": len(user_counts),
        "completed_by_user": user_counts
    }

    with open("todo_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nSummary report saved to todo_report.json")
except requests.RequestException:
    print("Could not connect to the API.")