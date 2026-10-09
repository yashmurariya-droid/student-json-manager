import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    todo = response.json()

    print("Task title:", todo.get("title", "Title unavailable"))

except requests.Timeout:
    print("The request took too long.")

except requests.HTTPError as e:
    print("HTTP error:", e.response.status_code)

except requests.RequestException:
    print("A network error occurred.")

except ValueError:
    print("The API returned invalid JSON.")