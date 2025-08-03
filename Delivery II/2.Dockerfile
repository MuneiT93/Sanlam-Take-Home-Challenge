FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install pandas openpyxl

CMD ["python", "ingest_sanctions.py"]
