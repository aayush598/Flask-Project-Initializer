def get_backend_structure(base_dir):
    backend_dir = f"{base_dir}/backend"

    directories = [
        f"{backend_dir}/app",
        f"{backend_dir}/app/blueprints",
        f"{backend_dir}/app/templates",
        f"{backend_dir}/app/static",
        f"{backend_dir}/tests",
        f"{backend_dir}/migrations",
        f"{backend_dir}/venv"
    ]

    files = {
        f"{backend_dir}/app/__init__.py": """from flask import Flask
from .config import Config
from .extensions import db, migrate
from .blueprints.example_blueprint import example

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(example)

    return app
""",
        f"{backend_dir}/app/routes.py": """from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello, World!"
""",
        f"{backend_dir}/app/models.py": """from .extensions import db

class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
""",
        f"{backend_dir}/app/extensions.py": """from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
""",
        f"{backend_dir}/app/config.py": """import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
""",
        f"{backend_dir}/app/blueprints/__init__.py": "",
        f"{backend_dir}/app/blueprints/example_blueprint.py": """from flask import Blueprint

example = Blueprint('example', __name__)

@example.route('/example')
def example_route():
    return "This is an example route."
""",
        f"{backend_dir}/app/templates/index.html": "<!DOCTYPE html>\n<html>\n<head>\n<title>Flask App</title>\n</head>\n<body>\n<div id='root'></div>\n</body>\n</html>",
        f"{backend_dir}/tests/__init__.py": "",
        f"{backend_dir}/tests/test_routes.py": """import unittest
from app import create_app, db
from app.models import ExampleModel

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)
""",
        f"{backend_dir}/tests/test_models.py": """import unittest
from app import create_app, db
from app.models import ExampleModel

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_example_model(self):
        with self.app.app_context():
            example = ExampleModel(name='Test Name')
            db.session.add(example)
            db.session.commit()
            self.assertEqual(ExampleModel.query.count(), 1)
            self.assertEqual(ExampleModel.query.first().name, 'Test Name')
""",
        f"{backend_dir}/requirements.txt": """Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
""",
        f"{backend_dir}/wsgi.py": """from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
""",
        f"{backend_dir}/manage.py": """from flask.cli import FlaskGroup
from app import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
""",
        f"{backend_dir}/.gitignore": """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Flask stuff:
instance/
.webassets-cache

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
.coverage
.pytest_cache/
.pytest_cache/*

# Translations
*.mo
*.pot

# Django stuff:
*.log

# Flask stuff:
env/
.venv/
env.bak/
venv.bak/
env.bak.bak/
venv.bak.bak/

# Virtualenv
venv/
venv.bak/
.env

# Editor files
.vscode/
.idea/
*.sublime-workspace
*.sublime-project

# OS generated files
.DS_Store
Thumbs.db
"""
    }

    return {'directories': directories, 'files': files}
