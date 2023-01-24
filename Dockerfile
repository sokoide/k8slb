FROM python:alpine

WORKDIR /app

COPY ./app /app

RUN pip install Flask werkzeug

CMD ["python", "main.py"]
