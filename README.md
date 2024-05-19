# Flask Backend Project Setup

This repository contains a script to automate the creation of a professional Flask backend project structure. It sets up the directory structure, essential files, and initial configurations to kickstart your Flask backend development process efficiently.

## Usage

1. Clone or download this repository.
2. Navigate to the directory containing the setup script.
3. Run the `setup.py` script using Python:
   ```sh
   python setup.py
4. Follow the instructions to complete the setup process.

## Folder Structure

The project structure is organized as follows:


- **`backend/`**: Main directory for the Flask backend.
  - **`app/`**: Contains the application modules.
    - **`blueprints/`**: Blueprints for organizing routes.
    - **`templates/`**: HTML templates for the application.
    - **`__init__.py`**: Initializes the Flask application.
    - **`config.py`**: Configuration settings for the application.
    - **`extensions.py`**: Initializes Flask extensions.
    - **`models.py`**: Defines database models.
    - **`routes.py`**: Defines application routes.
  - **`migrations/`**: Directory for database migrations.
  - **`tests/`**: Contains unit tests for the application.
    - **`__init__.py`**: Initializes the test package.
    - **`test_models.py`**: Unit tests for database models.
    - **`test_routes.py`**: Unit tests for application routes.
  - **`.gitignore`**: Specifies files and directories to be ignored by Git.
  - **`manage.py`**: Script for running Flask CLI commands.
  - **`requirements.txt`**: Lists Python dependencies required for the project.
  - **`wsgi.py`**: Entry point for the WSGI server.
- **`setup_flask_backend.py`**: Main script to initialize the Flask backend project.
- **`backend_structure.py`**: Defines the structure of the Flask backend project.
- **`file_utils.py`**: Utility functions for file system operations.

## Contributing

Contributions are welcome! Here's how you can contribute to this project:

1. **Fork** the repository on GitHub.
2. **Clone** the forked repository to your local machine.
   ```sh
   git clone https://github.com/aayush598/Flask-Project-Initializer.git
3. Create a new branch for your feature or bug fix.
    ```sh
    git checkout -b feature-or-bug-fix
4. Make changes to the codebase.
5. Test your changes to ensure they work as expected.
6. Commit your changes with descriptive commit messages.
    ```sh
    git commit -am 'Add new feature' 
7. Push your changes to your forked repository.
    ```sh
    git push origin feature-or-bug-fix
8. Open a Pull Request (PR)
    - Go to the GitHub page of your forked repository.
    - Click on the "New Pull Request" button.
    - Provide a descriptive title and summary of your changes in the PR description.
    - Click on "Create Pull Request" to submit your contribution for review.

Please ensure that your contributions adhere to the project's coding standards and conventions. Also, make sure to test your changes thoroughly before submitting a pull request. Thank you for contributing to this project!

## License

This project is licensed under the [MIT License](LICENSE).

## Author

[Aayush Gid](https://github.com/aayush598)
