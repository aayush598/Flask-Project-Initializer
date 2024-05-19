import os

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def create_files(files):
    for path, content in files.items():
        create_file(path, content)
