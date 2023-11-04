import socket
from pathlib import Path

SERVER_ADDRESS = Path('./emailer_socket')


def start_emailer(sqla_uri: str):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        try:
            s.connect(SERVER_ADDRESS.name)
        except socket.error as msg:
            raise msg
        try:
            s.send(sqla_uri.encode("utf-8"), 8914)
        finally:
            return s.recv(256)
