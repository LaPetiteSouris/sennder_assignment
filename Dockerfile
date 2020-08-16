FROM python:3.7.3-slim

COPY . /sennder

WORKDIR  /sennder

RUN pip3 install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8000 -w 2 --threads 2 --access-logfile - "api.wsgi:app"