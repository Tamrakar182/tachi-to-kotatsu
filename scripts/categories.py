import json
import time
import os

file_path = "output.json"

with open(file_path, "r") as file:
    data = json.load(file)

results = []

for entry in data["backupCategories"]:
    name = entry['name']
    order = entry.get('order', 0)
    results.append((name, order))

#  Category Structure from Kotatsu
#  {
#     "category_id": 1,
#     "created_at": 1704781699296,
#     "sort_key": "<Order>",
#     "title": "<Name>",
#     "order": "NEWEST",
#     "track": true,
#     "show_in_lib": true
# }
    
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

with open(new_file_path, 'w') as f:
    json.dump(categories, f, indent=2)