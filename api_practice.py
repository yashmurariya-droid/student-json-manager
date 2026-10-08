import requests

try:
    url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(url)

    response.raise_for_status()

    todos = response.json()

    completed = 0
    pending = 0

    for todo in todos:
        if todo["completed"]:
            completed += 1
        else:
            pending += 1

    print("Total todos:", len(todos))
    print("Completed:", completed)
    print("Pending:", pending)

    completion_rate = (completed / len(todos)) * 100

    print("Completion rate:", completion_rate, "%")

except requests.RequestException:
    print("Could not connect to the API.")