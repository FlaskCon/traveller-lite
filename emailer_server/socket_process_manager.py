import multiprocessing
from pathlib import Path
from typing import Optional

from sqlalchemy import create_engine, text, Engine

from email_service import EmailService, EmailServiceSettings
from socket_types import Job


class SocketProcessManager:
    socket_address: Path
    email_service: Optional[EmailService]
    email_service_settings: Optional[EmailServiceSettings]
    sql_engine: Optional[Engine]
    sql_database_uri: Optional[str]
    processes: list[multiprocessing.Process]

    sql_connection_ok: bool
    email_connection_ok: bool

    def __init__(
            self,
            socket_address: Path,
            email_service_settings: Optional[EmailServiceSettings] = None,
            sql_database_uri: Optional[str] = None,
            sql_in_memory: bool = False
    ):

        self.socket_address = socket_address

        if email_service_settings:
            self.email_service_settings = email_service_settings
            self.email_service = EmailService(email_service_settings)
        else:
            self.email_service_settings = None
            self.email_service = None

        if sql_in_memory:
            sql_database_uri = "sqlite:///:memory:"

        if sql_database_uri:
            self.sql_database_uri = sql_database_uri
            self.sql_engine = create_engine(
                sql_database_uri,
                echo=False
            )

            if sql_in_memory:
                with self.sql_engine.connect() as connection:
                    with connection.begin():
                        connection.execute(
                            text(
                                "create table email_queue ( email_id INTEGER not null primary key, "
                                "email_to VARCHAR, email_subject VARCHAR, email_message VARCHAR, "
                                "staged BOOLEAN not null, created DATETIME not null);"
                            )
                        )

        else:
            self.sql_database_uri = None
            self.sql_engine = None

        self.processes = []

        self.email_connection_ok = False
        self.sql_connection_ok = False

    def __call__(self, job: Job) -> int | None:

        if job is Job.REPROCESS:
            sql_find = "SELECT email_id, email_to, email_subject, email_message FROM email_queue WHERE staged = true;"
        else:
            sql_find = "SELECT email_id, email_to, email_subject, email_message FROM email_queue WHERE staged = false;"

        with self.sql_engine.connect() as connection:
            emails_found = connection.execute(text(sql_find))

        emails_to_be_sent = [(email[0], email[1], email[2], email[3]) for email in emails_found]

        if job is Job.PROCESS:
            if emails_to_be_sent:
                with self.sql_engine.connect() as connection:
                    with connection.begin():
                        connection.execute(text("UPDATE email_queue SET staged = true WHERE staged = false;"))

        return self.create_process(self.send_emails, (self.sql_engine, emails_to_be_sent))

    def set_sql_engine(self, database_uri: str) -> None:
        self.sql_database_uri = database_uri
        self.sql_engine = create_engine(
            database_uri,
            echo=False
        )

    def set_email_service(self, email_service_settings: EmailServiceSettings) -> None:
        self.email_service_settings = email_service_settings
        self.email_service = EmailService(email_service_settings)

    def test_sql_connection(self) -> bool:
        try:
            with self.sql_engine.connect() as connection:
                connection.execute(text("SELECT 1;"))
                return True
        except Exception as error:
            _ = error
            return False

    def test_email_connection(self) -> bool:
        try:
            self.email_service.test_connection()
            return True
        except Exception as error:
            _ = error
            return False

    def create_process(self, target: callable, args: tuple) -> int | None:
        process = multiprocessing.Process(target=target, args=args)
        self.processes.append(process)
        process.start()
        return process.pid

    def cleanup_processes(self) -> None:
        for index, process in enumerate(self.processes):
            if not process.is_alive():
                self.processes.pop(index)

    def send_emails(self, engine: Engine, emails_to_be_sent: list[tuple[str, str, str, str]]):

        for email in emails_to_be_sent:

            email_id = email[0]
            email_to = email[1]
            email_subject = email[2]
            email_message = email[3]

            if engine.echo:
                print(" " * 50)
                print(f"Sending email to {email_to}")
                print(f"Subject: {email_subject}")
                print(f"Body: {email_message}")

            self.email_service.recipients([email_to]).subject(email_subject).body(email_message).send()

            with engine.connect() as connection:
                with connection.begin():
                    connection.execute(
                        text("DELETE FROM email_queue WHERE email_id = :email_id;").bindparams(email_id=email_id)
                    )
