from pathlib import Path
from threading import Thread

from sqlalchemy import create_engine, text, Engine

from email_service import EmailService, EmailServiceSettings
from socket_types import Job


class SocketProcess:
    email_settings: EmailServiceSettings
    socket_address: Path
    threads: list[Thread]

    def __init__(self, email_settings: EmailServiceSettings, socket_address: Path):
        self.email_settings = email_settings
        self.socket_address = socket_address
        self.threads = []

    def __call__(self, database_uri: str, job: Job):

        engine = create_engine(database_uri, echo=False)

        if job is Job.REPROCESS:
            sql_find = "SELECT email_id, email_to, email_subject, email_message FROM email_queue WHERE staged = true;"
        else:
            sql_find = "SELECT email_id, email_to, email_subject, email_message FROM email_queue WHERE staged = false;"

        with engine.connect() as connection:
            emails_found = connection.execute(text(sql_find))

        emails_to_be_sent = [(email[0], email[1], email[2], email[3]) for email in emails_found]

        if job is Job.PROCESS:
            if emails_to_be_sent:
                with engine.connect() as connection:
                    with connection.begin():
                        connection.execute(text("UPDATE email_queue SET staged = true WHERE staged = false;"))

        self.create_thread(self.send_emails, (engine, emails_to_be_sent))

    def create_thread(self, target: callable, args: tuple):
        thread = Thread(daemon=True, target=target, args=args)
        self.threads.append(thread)
        thread.start()

    def send_emails(self, engine: Engine, emails_to_be_sent: list[tuple[str, str, str, str]]):

        for email in emails_to_be_sent:

            email_id = email[0]
            email_to = email[1]
            email_subject = email[2]
            email_message = email[3]

            email_service = EmailService(self.email_settings)

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
