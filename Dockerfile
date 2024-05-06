FROM flaskcon/base-layer:latest
COPY .env .env
COPY app app
RUN mkdir -p app/instance
COPY configs/gunicorn.conf.py gunicorn.conf.py
COPY configs/supervisor.ini supervisor.ini
COPY configs/supervisord.conf supervisord.conf

ENTRYPOINT ["supervisord", "-c", "/traveller-lite/supervisord.conf"]
