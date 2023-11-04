import signal
import socket
import sys
from pathlib import Path

from email_service import EmailService, EmailServiceSettings
from socket_process import SocketProcess
from socket_types import Job


class SocketServer:
    socket_address: Path
    email_settings: EmailServiceSettings
    email_connection_ok: bool
    socket: socket.socket

    processing_fetch: bool = False
    socket_process: SocketProcess
    process_job: Job

    data_collection: list[bytes]

    def __init__(self, socket_address: Path, email_settings: EmailServiceSettings, socket_process: SocketProcess):
        self.socket_address = socket_address
        self.email_settings = email_settings

        self.socket_process = socket_process

        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.data_collection = []
        self.threads = []

        self.email_connection_ok = self.test_email_connection()

        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, _, __):
        print("\nShutting down server")
        self.socket_address.unlink(missing_ok=True)
        sys.exit(0)

    def test_email_connection(self):
        email_service = EmailService(self.email_settings)
        return email_service.test_connection()

    def listen_for_data(self, connection):
        while True:

            data = connection.recv(256)
            decoded_data = data.decode("utf-8")

            if "PROCESS" in decoded_data or "REPROCESS" in decoded_data:
                self.process_job = Job.REPROCESS if "REPROCESS" in decoded_data else Job.PROCESS

                self.data_collection.append(decoded_data)

                if not self.email_connection_ok:
                    connection.sendall(b"ERROR")
                else:
                    connection.sendall(b"OK")
                    break

            if not data:
                break

    def start(self):
        self.processing_fetch = False
        self.socket_address.unlink(missing_ok=True)

        with self.socket as socket_:
            print(f"Starting up on {self.socket_address.name}")

            socket_.bind(self.socket_address.name)
            socket_.listen(8914)

            while True:

                connection, _ = socket_.accept()

                try:

                    self.listen_for_data(connection)

                finally:

                    if self.email_connection_ok:
                        _, database_uri = self.data_collection[0].split("~")
                        self.socket_process(database_uri, self.process_job)
                        self.data_collection = []

                    connection.close()
