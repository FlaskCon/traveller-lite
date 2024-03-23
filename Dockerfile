FROM flaskcon/base-layer:latest
COPY .env .env
COPY app app
RUN mkdir -p app/instance
COPY gunicorn.conf.py gunicorn.conf.py
COPY supervisor.ini supervisor.ini
COPY supervisord.conf supervisord.conf
RUN flask seed

ENTRYPOINT ["supervisord", "-c", "/traveller-lite/supervisord.conf"]
