from utils import create_directories, create_files
from structure import get_backend_structure

def create_flask_backend_structure(base_dir):
    backend_structure = get_backend_structure(base_dir)

    # Create directories
    create_directories(backend_structure['directories'])

    # Create files with content
    create_files(backend_structure['files'])

if __name__ == "__main__":
    base_dir = "test123"
    create_flask_backend_structure(base_dir)
    print(f"Backend project structure created at {base_dir}/backend")