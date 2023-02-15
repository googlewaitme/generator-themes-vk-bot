FROM python:3.8-slim-buster

WORKDIR /app/

RUN addgroup --system app && adduser --system --group app --home /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

COPY src/ .

RUN python make_migrations.py

ENTRYPOINT ["python", "app.py"]
