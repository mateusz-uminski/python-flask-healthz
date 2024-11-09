# python-flask-healthz

[![verify](https://github.com/mateusz-uminski/python-flask-healthz/actions/workflows/verify.yaml/badge.svg)](https://github.com/mateusz-uminski/python-flask-healthz/actions/workflows/verify.yaml)

This is a lightweight Flask application that provides a simple health check API endpoint. The application exposes a `/api/v1/healthz` endpoint that returns the service's health status. The endpoint can be used to verify if the application is running and operational.

Besides the README.md further documentation can be found in commits, code comments and nested README files.

Feel free to explore and copy everything you want. Enjoy!


# Prerequisites

```sh
poetry install --no-root
```


# Usage

## Run the application

```sh
poetry run python -m app.app
```

## Run tests

```sh
poetry run pytest --cov=app --cov-report=html --cov-report=term
```

## Build a docker image

```sh
docker build -t python-flask-healthz .
```

## Run the docker image

```sh
docker run -p 8080:8080 python-flask-healthz
```

## Example query

```sh
curl -v -XGET 127.0.0.1:8080/api/v1/healthz
```
