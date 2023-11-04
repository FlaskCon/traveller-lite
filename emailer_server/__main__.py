import os
import signal
import socket
import sys
from pathlib import Path
from threading import Thread

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

from email_service import EmailService, EmailServiceSettings

load_dotenv()

email_settings = EmailServiceSettings(
    int(os.environ.get("EMAIL_DEV_MODE")),
    os.environ.get("EMAIL_USERNAME"),
    os.environ.get("EMAIL_PASSWORD"),
    os.environ.get("EMAIL_SERVER"),
    int(os.environ.get("EMAIL_PORT")),
)

SERVER_ADDRESS = Path('./emailer_socket')


def signal_handler(_, __):
    print("\nShutting down server")
    SERVER_ADDRESS.unlink(missing_ok=True)
    sys.exit(0)


def daemon_task(connection):
    engine = create_engine(connection, echo=True)

    with engine.connect() as connection:
        with connection.begin():
            to_be_sent = connection.execute(
                text("SELECT * FROM email_queue WHERE staged = false;")
            ).fetchall()

    with engine.connect() as connection:
        with connection.begin():
            for email in to_be_sent:
                connection.execute(
                    text("UPDATE email_queue SET staged = true WHERE email_id = :email_id;").bindparams(
                        email_id=email[0]
                    )
                )

    for email in to_be_sent:
        email_service = EmailService(email_settings)
        if engine.echo:
            print(" " * 50)
            print(f"Sending email to {email[1]}")
            print(f"Subject: {email[2]}")
            print(f"Body: {email[3]}")
        email_service.recipients([email[1]]).subject(email[2]).body(email[3]).send()

        with engine.connect() as connection:
            with connection.begin():
                connection.execute(
                    text("UPDATE email_queue SET sent = true WHERE email_id = :email_id;").bindparams(
                        email_id=email[0]
                    )
                )


signal.signal(signal.SIGINT, signal_handler)


def start_server():
    SERVER_ADDRESS.unlink(missing_ok=True)

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        print(f"Starting up on {SERVER_ADDRESS.name}")
        s.bind(SERVER_ADDRESS.name)
        s.listen(8914)
        while True:

            connection, _ = s.accept()
            data_collection = []

            try:
                while True:
                    data = connection.recv(256)

                    data_collection.append(data)

                    if data:
                        connection.sendall(data)
                    else:
                        break

            finally:

                thread = Thread(daemon=True, target=daemon_task, args=(data_collection[0].decode("utf-8"),))
                thread.start()

                connection.close()


if __name__ == "__main__":
    start_server()
