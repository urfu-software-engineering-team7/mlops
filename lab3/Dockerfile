FROM python:3.9

RUN apt update

RUN apt install uvicorn -y

RUN mkdir -m 777 /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
