import json
import time
import os

file_path = "output.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error decoding JSON from '{file_path}'.")
    exit(1)

results = []

for entry in data.get("backupCategories", []):
    name = entry['name']
    order = entry.get('order', 0)
    results.append((name, order))

categories = [
    {
        "category_id": i + 1,
        "created_at": int(time.time() * 1000),
        "sort_key": order,
        "title": name,
        "order": "NEWEST",
        "track": True,
        "show_in_lib": True
    }
    for i, (name, order) in enumerate(results)
]

new_file_path = os.path.join('./result/', 'categories')

os.makedirs(os.path.dirname(new_file_path), exist_ok=True)

try:
    with open(new_file_path, 'w') as f:
        json.dump(categories, f, indent=2)
except PermissionError:
    print(f"Permission denied for '{new_file_path}'.")
    exit(1)
except Exception as e:
    print(f"An error occurred while writing to '{new_file_path}': {e}")
    exit(1)