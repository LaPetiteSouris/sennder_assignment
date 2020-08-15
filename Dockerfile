FROM python:3.7.3-slim

COPY . /sennder

WORKDIR  /sennder

RUN pip3 install -r requirements.txt
RUN pwd 
CMD gunicorn -b 0.0.0.0:3000 -w 2 --threads 2 --access-logfile - "api.wsgi:app"
#CMD sleep 300