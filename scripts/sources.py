import json
import os

with open('output.json') as f:
    data = json.load(f)

names = [source['name'].upper() for source in data.get('backupSources', [])]

with open('./defaults/sources') as f:
    sources = json.load(f)

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

with open(new_file_path, 'w') as f:
    json.dump(sources, f, indent=2)
