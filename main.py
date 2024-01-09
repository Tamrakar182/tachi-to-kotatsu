import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py <file_path>")
    sys.exit(1)

# Use sys.executable to get the path of the current Python interpreter
python_interpreter = sys.executable

file_path = sys.argv[1]

# Step 1: Run unzip.py to unzip the tachi file
print("Unzipping file...")
subprocess.run([python_interpreter, './scripts/unzip.py', file_path])
print("Unzipped serialised .proto file")

# Step 2: Run decoder.py to decode the generated tachi.proto file
print("Deserialising .proto file...")
subprocess.run([python_interpreter, './scripts/decoder.py'])
print("Generated output.json file")

# Step 3: Run various scripts to generate the required files
print("Generating kotatsu files...")
subprocess.run([python_interpreter, './scripts/categories.py'])
subprocess.run([python_interpreter, './scripts/sources.py'])
subprocess.run([python_interpreter, './scripts/settings.py'])
print("Generated kotatsu files")

# Step 4: Run zip.py to zip to get the kotatsu zip
print("Zipping files...")
subprocess.run([python_interpreter, './scripts/zip.py'])
print("Zipped kotatsu file")

# Step 5: Cleanup
print("Cleaning up...")
subprocess.run([python_interpreter, './scripts/cleanup.py'])
print("Cleaned up")

print("Done!")
