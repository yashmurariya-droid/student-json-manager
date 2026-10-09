import requests


def fetch_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        todo = response.json()

        if not isinstance(todo, dict):
            print("Unexpected API data format.")
            return

        print("Task ID:", todo.get("id", "ID unavailable"))
        print("Title:", todo.get("title", "Title unavailable"))
        print("Completed:", todo.get("completed", "Status unavailable"))

    except requests.Timeout:
        print("The API took too long to respond.")

    except requests.HTTPError as e:
        print("HTTP error:", e.response.status_code)

    except requests.RequestException:
        print("A network error occurred.")

    except ValueError:
        print("The API returned invalid JSON.")


fetch_todo()