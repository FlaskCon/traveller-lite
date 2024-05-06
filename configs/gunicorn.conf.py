from os import cpu_count

bind = "0.0.0.0:5000"
workers = cpu_count() * 2 + 1
wsgi_app = "app:create_app()"
errorlog = "gunicorn_error.log"
accesslog = "gunicorn_access.log"