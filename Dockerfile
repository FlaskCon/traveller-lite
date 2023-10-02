FROM python:3.11-alpine
WORKDIR /traveller-lite
RUN apk update && apk upgrade
RUN apk add --no-cache tzdata
ENV TZ=Europe/London
# See here for timezones:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
COPY .env .env
COPY app app
COPY gunicorn.conf.py gunicorn.conf.py
COPY supervisor.ini supervisor.ini
COPY supervisord.conf supervisord.conf
COPY requirements.txt requirements.txt
COPY requirements-docker.txt requirements-docker.txt
RUN python3 -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install -r requirements-docker.txt

ENTRYPOINT ["/traveller-lite/venv/bin/supervisord", "-c", "/traveller-lite/supervisord.conf"]
