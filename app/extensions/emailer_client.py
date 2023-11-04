import socket
from pathlib import Path
from typing import Literal

SERVER_ADDRESS = Path('./emailer_socket')


def start_emailer(message: str, processor: Literal["REPROCESS", "PROCESS"] = "PROCESS"):
    send_message = f"{processor}~{message}"

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        try:
            s.connect(SERVER_ADDRESS.name)
        except socket.error as msg:
            raise msg
        try:
            s.send(send_message.encode("utf-8"), 8914)
        finally:
            return s.recv(256)
