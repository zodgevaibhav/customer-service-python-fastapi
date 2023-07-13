# Untested yet
FROM python:3.8-slim

RUN apt-get update && apt-get upgrade -y

RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./

# Copy Pipfile.lock to make sure all transitive dependencies are same as development
COPY Pipfile.lock ./

# Install project dependencies using pipenv
RUN pipenv install --deploy --ignore-pipfile

COPY . .

# Start the FastAPI application (since our main file is in app folder will have to give app.main)
CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]