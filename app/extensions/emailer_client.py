import socket
from pathlib import Path
from typing import Literal

SERVER_ADDRESS = Path("./emailer_socket")


def start_emailer(
    database_uri: str, processor: Literal["REPROCESS", "PROCESS"] = "PROCESS"
):
    send_message = f"{processor}~{database_uri}"

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        try:
            s.connect(SERVER_ADDRESS.name)
        except socket.error as msg:
            raise msg
        try:
            s.send(send_message.encode("utf-8"), 8914)
        finally:
            return s.recv(256).decode("utf-8")


def kill_process(pid: str):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        try:
            s.connect(SERVER_ADDRESS.name)
        except socket.error as msg:
            raise msg
        try:
            s.send(f"KILL~{pid}".encode("utf-8"), 8914)
        finally:
            return s.recv(256).decode("utf-8")
