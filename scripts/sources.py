import json
import os

try:
    with open('output.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File 'output.json' not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding JSON from 'output.json'.")
    exit(1)

names = [source['name'].upper() for source in data.get('backupSources', [])]

try:
    with open('./defaults/sources') as f:
        sources = json.load(f)
except FileNotFoundError:
    print("File './defaults/sources' not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding JSON from './defaults/sources'.")
    exit(1)

for source in sources:
    source['enabled'] = source['source'] in names

enabled_counter = 1
disabled_counter = len(sources) + 1
for source in sources:
    source['enabled'] = source['source'] in names
    if source['enabled']:
        source['sort_key'] = enabled_counter
        enabled_counter += 1
    else:
        source['sort_key'] = disabled_counter
        disabled_counter -= 1

new_file_path = os.path.join('./result/', 'sources')

try:
    with open(new_file_path, 'w') as f:
        json.dump(sources, f, indent=2)
except FileNotFoundError:
    print(f"Directory './result/' not found.")
    exit(1)
except PermissionError:
    print(f"Permission denied for {new_file_path}.")
    exit(1)