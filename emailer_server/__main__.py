import os
from pathlib import Path

from dotenv import load_dotenv

from email_service import EmailServiceSettings
from socket_process_manager import SocketProcessManager
from socket_server import SocketServer

load_dotenv()

email_settings = EmailServiceSettings(
    int(os.environ.get("EMAIL_DEV_MODE")),
    os.environ.get("EMAIL_USERNAME"),
    os.environ.get("EMAIL_PASSWORD"),
    os.environ.get("EMAIL_SERVER"),
    int(os.environ.get("EMAIL_PORT")),
)

if __name__ == "__main__":
    socket_address = Path('./emailer_socket')

    socket_server = SocketServer(
        socket_address,
        email_settings
    )
    socket_server.start()
