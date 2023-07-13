FROM python:3.8-slim

RUN apt-get update && apt-get upgrade -y

RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

