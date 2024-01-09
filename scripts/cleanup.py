import os
import shutil

result_path = "./result"
output_path = "./output.json"
files_path = "./files"

if os.path.exists(result_path):
    shutil.rmtree(result_path)
else:
    raise Exception("Result directory does not exist")

if os.path.exists(output_path):
    os.remove(output_path)
else:
    raise Exception("Output file does not exist")

if os.path.exists(files_path):
    shutil.rmtree(files_path)
else:
    raise Exception("Files directory does not exist")
