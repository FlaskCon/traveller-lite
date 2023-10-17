import random
import time
import timeit

from flask import Flask, g

template = """\
<html>
    <head>
        <title>Flask Request Timer</title>
    </head>
    <body>
        <p>See terminal</p>
    </body>
</html>
"""


def create_app():
    app = Flask(__name__)

    app.secret_key = "secret_key"

    @app.before_request
    def before_request():
        g.start_time = timeit.default_timer()
        g.request_id = random.randrange(int("1" * 8), int("9" * 8))
        return None

    @app.get("/")
    def time_me():
        time.sleep(2)
        return template

    @app.after_request
    def after_request(response):
        stop_time = timeit.default_timer()
        print(f"Request ID: {g.request_id} - Time taken: {round(stop_time - g.start_time, 5)} seconds")
        return response

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
