import os
import signal
import socket
import sys
from pathlib import Path
from threading import Thread
from time import sleep

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

PROCESSING_SQL = False


def signal_handler(_, __):
    print("\nShutting down server")
    SERVER_ADDRESS.unlink(missing_ok=True)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def process(connection, processor="PROCESS"):
    global PROCESSING_SQL

    engine = create_engine(connection, echo=True)

    PROCESSING_SQL = True

    if processor == "REPROCESS":
        sql_find = "SELECT email_id, email_to, email_subject, email_message FROM email_queue WHERE staged = true;"
    else:
        sql_find = "SELECT email_id, email_to, email_subject, email_message FROM email_queue WHERE staged = false;"

    with engine.connect() as connection:
        with connection.begin():
            emails_found = connection.execute(text(sql_find))

    emails_to_be_sent = [(email[0], email[1], email[2], email[3]) for email in emails_found]

    if processor != "REPROCESS":
        if emails_to_be_sent:
            with engine.connect() as connection:
                with connection.begin():
                    connection.execute(text("UPDATE email_queue SET staged = true WHERE staged = false;"))

    PROCESSING_SQL = False

    for email in emails_to_be_sent:

        email_id = email[0]
        email_to = email[1]
        email_subject = email[2]
        email_message = email[3]

        email_service = EmailService(email_settings)

        if engine.echo:
            print(" " * 50)
            print(f"Sending email to {email_to}")
            print(f"Subject: {email_subject}")
            print(f"Body: {email_message}")

        email_service.recipients([email_to]).subject(email_subject).body(email_message).send()

        with engine.connect() as connection:
            with connection.begin():
                connection.execute(
                    text("DELETE FROM email_queue WHERE email_id = :email_id;").bindparams(email_id=email_id)
                )


def start_server():
    global PROCESSING_SQL

    SERVER_ADDRESS.unlink(missing_ok=True)

    email_service = EmailService(email_settings)

    if email_service.test_connection():
        email_connection = True
    else:
        email_connection = False

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
                        if not email_connection:
                            connection.sendall(b"ERROR")
                        else:
                            connection.sendall(b"OK")
                    else:
                        break

            finally:

                if email_connection:

                    while True:
                        sleep(1)
                        if not PROCESSING_SQL:
                            break

                    processor, uri = data_collection[0].decode("utf-8").split("~")

                    thread = Thread(daemon=True, target=process, args=(uri, processor,))
                    thread.start()

                connection.close()


if __name__ == "__main__":
    start_server()
