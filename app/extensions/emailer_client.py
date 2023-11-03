import signal
import socket
import sys
from hashlib import sha256
from pathlib import Path

from flask import current_app as app

from app.models.email_queue import EmailQueue


def signal_handler(_, __):
    print("\nShutting down server")
    sys.exit(0)


SERVER_ADDRESS = Path('./emailer_socket')
signal.signal(signal.SIGINT, signal_handler)


def send_enqueued_email(email_id: int, email_address: str):
    uid = sha256(f"{email_id}+{email_address}".encode()).hexdigest()

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        try:
            s.connect(SERVER_ADDRESS.name)
        except socket.error as msg:
            raise msg

        try:
            message = uid.encode("utf-8")
            print(f"Sending uid: {message}")
            s.sendall(message)
            with app.app_context():
                EmailQueue.update_uid(email_id, uid)
            data = s.recv(256)
            print(f"Received uid: {data}")

        finally:
            print("closing socket")
