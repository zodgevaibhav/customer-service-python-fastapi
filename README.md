# Project
- This is template project to being implementaion of API using `fastapi` and related libraries

# Project Folder Structure

Let's briefly explain each folder:

- `app`: This folder contains the main application code.
    - `api`: This folder houses the API-related code.
        - `endpoints`: It contains your FastAPI route definitions.
        - `models`: This is where you define your data models or schemas.
    - `core`: It contains the core application logic.
        - `event_handlers`: This folder holds event handlers or listeners.
        - `event_schemas`: Here, you define schemas for the event payloads.
        - `repositories`: It contains data access and persistence logic.
    - `db`: This folder can contain database-related files, such as migrations.
    - `services`: Here, you can define any additional services or helper classes.
    - `utils`: This folder can hold utility functions or modules.
    - `main.py`: The entry point of your FastAPI application.
    - `settings.py`: Configuration settings for your application.

- `tests`: This folder contains your test files.

- `.env`: This file can store environment variables for local development.

- `.gitignore`: A file that specifies which files and folders to exclude from version control.

- `pipfile`: The configuration file for your Python project.

- `pipfile.lock`: The Pipfile.lock file is needed for reproducible and consistent dependency management in Python projects, ensuring that the same versions of dependencies are installed across different environments, improving efficiency, security, and collaboration

- `README.md`: A documentation file explaining your project.


# Install project dependencies

- The `pipenv install` command is used to install project dependencies within a virtual environment.
- The `pipenv install --system` command is used to install project dependencies globally on your system rather than within a virtual environment.

# Activate the virtual environment
- To activate pipenv and enter the virtual environment associated with your project run the `pipenv shell` command

# Run the api using uvicorn server
- command `uvicorn main:app --reload` (working directory should be `app` while executing this command )
- `uvicorn`: This is the command to run the Uvicorn server.
- `main:app`: Replace `main` with the name of your Python file (without the `.py` extension) that contains the application code. Replace `app` with the name of the FastAPI instance or the application object within that file.
- `--reload`: This flag enables automatic reloading of the server when code changes are detected. It's useful during development as it automatically restarts the server whenever you make changes to your application code, allowing you to see the changes immediately without manually restarting the server.



