FROM python:3.9-bullseye

RUN mkdir -m 777 /app

WORKDIR /app

COPY . /app

RUN pip install poetry==1.4.0

RUN poetry --no-root install

ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
