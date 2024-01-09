from google.protobuf.json_format import MessageToDict
from tachi_classes_pb2 import Backup
import json

backup = Backup()
path = './files/tachi.proto'

try:
    with open(path, 'rb') as f:
        backup.ParseFromString(f.read())
except FileNotFoundError:
    print(f"File '{path}' not found.")
    exit(1)
except Exception as e:
    print(f"An error occurred while parsing: {e}")
    exit(1)

try:
    data = json.loads(json.dumps(MessageToDict(backup)))
except json.JSONDecodeError:
    print("Error decoding JSON.")
    exit(1)

try:
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=4)
except PermissionError:
    print("Permission denied for 'output.json'.")
    exit(1)
except Exception as e:
    print(f"An error occurred while writing to 'output.json': {e}")
    exit(1)