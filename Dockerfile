# syntax=docker/dockerfile:1
FROM python:3.9.13-slim-buster

WORKDIR /viribus-unitis_backend
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY backend/ .

CMD python3 -m uvicorn app:app --host=0.0.0.0 --port=80