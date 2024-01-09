from tachi_classes_pb2 import Backup
import json
from google.protobuf.json_format import MessageToDict

backup = Backup()
path = './files/tachi.proto'

with open(path, 'rb') as f:
    backup.ParseFromString(f.read())

data = json.loads(json.dumps(MessageToDict(backup)))

# Write the dictionary to a JSON file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)
