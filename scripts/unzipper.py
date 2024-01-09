import zipfile
import gzip
import shutil

def unzip_file(file_path, output_dir):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def gunzip_file(file_path, output_file_path):
    with gzip.open(gzip_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# zip_file_path = './files/kotatsu.zip'
# output_dir = './files'
# unzip_file(zip_file_path, output_dir)

gzip_file_path = './files/tachi.proto.gz'
output_file_path = './files/tachi.proto'
gunzip_file(gzip_file_path, output_file_path)
