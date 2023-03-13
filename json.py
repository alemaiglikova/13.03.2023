import requests
import json

for i in range(1, 11):
    url = f"https://jsonplaceholder.typicode.com/todos/{i}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(f"data{i}.json", "w") as f:
            json.dump(data, f)