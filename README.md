## API Todo Analytics Tool

A beginner Python project that retrieves todo records from a REST API, filters completed tasks, analyzes the results, and saves reports as JSON files.

### Features

* Fetches todo records using the `requests` library
* Filters completed tasks using Python loops and conditions
* Saves completed records to `completed_todos.json`
* Loads and verifies saved JSON data
* Counts completed tasks for each user
* Generates a summary report in `todo_report.json`
* Handles API request errors

### Technologies

* Python
* Requests
* REST APIs and HTTP
* JSON
* Lists, dictionaries, loops, and exception handling

### How to Run

1. Install Requests: `python -m pip install requests`
2. Run: `python api_practice.py`
3. The program generates `completed_todos.json` and `todo_report.json`.

Note: The JSON files are generated locally when the program runs.
