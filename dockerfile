# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 9090
EXPOSE 9100
EXPOSE 9093
COPY . .
CMD ["flask", "run"]