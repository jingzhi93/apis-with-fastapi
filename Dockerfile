FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

COPY requirements-docker.txt /app

RUN pip --no-cache-dir install -r requirements-docker.txt 