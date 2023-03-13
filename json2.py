import requests
import json
import threading
import asyncio
import multiprocessing


def get_data(id):
    url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(f"data{id}.json", "w") as f:
            json.dump(data, f)

threads = []

for i in range(1, 11):
    thread = threading.Thread(target=get_data, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()







def get_data(id):
    url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(f"data{id}.json", "w") as f:
            json.dump(data, f)

processes = []

for i in range(1, 11):
    process = multiprocessing.Process(target=get_data, args=(i,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()









async def get_data(id):
    url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    if response.status_code == 200:
        data = response.json()
        with open(f"data{id}.json", "w") as f:
            json.dump(data, f)

async def main():
    tasks = [asyncio.create_task(get_data(i)) for i in range(1, 11)]
    await asyncio.gather(*tasks)

asyncio.run(main())