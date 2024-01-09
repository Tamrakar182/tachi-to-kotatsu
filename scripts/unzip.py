import sys
import gzip
import shutil
import os

def gunzip_file(gzip_file_path, output_file_path):
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with gzip.open(gzip_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

if len(sys.argv) != 2:
    print("Usage: python unzipper.py <gzip_file_path>")
    sys.exit(1)

gzip_file_path = sys.argv[1]
output_file_path = './files/tachi.proto'
gunzip_file(gzip_file_path, output_file_path)