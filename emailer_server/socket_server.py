import signal
import socket
import sys
from pathlib import Path

from email_service import EmailServiceSettings
from socket_process_manager import SocketProcessManager
from socket_types import Job


class SocketServer:
    socket_address: Path
    email_settings: EmailServiceSettings
    socket: socket.socket
    socket_process_manager: SocketProcessManager

    process_job: Job

    def __init__(self, socket_address: Path, email_settings: EmailServiceSettings):
        self.socket_address = socket_address
        self.email_settings = email_settings

        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.data_collection = []
        self.threads = []

        self.socket_process_manager = SocketProcessManager(socket_address, email_settings)

        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, _, __):
        print("\nShutting down server")
        self.socket_address.unlink(missing_ok=True)
        sys.exit(0)

    def listen_for_data(self, connection):
        while True:

            data = connection.recv(256)
            decoded_data = data.decode("utf-8")

            if "KILL" in decoded_data:
                _, pid = decoded_data.split("~")

                found = False

                for process in self.socket_process_manager.processes:
                    if process.pid == int(pid):
                        found = True
                        process.terminate()
                        connection.sendall(b"TERMINATED")
                        break

                if not found:
                    connection.sendall(b"NOTFOUND")
                    break

            if "PROCESS" in decoded_data:

                self.process_job = Job.REPROCESS if "REPROCESS" in decoded_data else Job.PROCESS

                _, database_uri = decoded_data.split("~")

                self.socket_process_manager.set_sql_engine(database_uri)

                if (
                        self.socket_process_manager.test_email_connection()
                        and self.socket_process_manager.test_sql_connection()
                ):
                    process_id = self.socket_process_manager(self.process_job)
                    connection.sendall(str(process_id).encode("utf-8"))
                else:
                    connection.sendall(b"ERROR")
                break

            if not data:
                break

    def start(self):
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

                    self.socket_process_manager.cleanup_processes()

                    connection.close()
