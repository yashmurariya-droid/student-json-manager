import requests

url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("Request successful!")

except requests.HTTPError as e:
    print("HTTP error:", e.response.status_code)

except requests.Timeout:
    print("The request took too long.")

except requests.RequestException:
    print("A network error occurred.")