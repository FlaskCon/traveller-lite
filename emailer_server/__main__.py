import signal
import socket
import sys
from pathlib import Path
from multiprocessing import Process

def signal_handler(_, __):
    print("\nShutting down server")
    sys.exit(0)


SERVER_ADDRESS = Path('./emailer_socket')
signal.signal(signal.SIGINT, signal_handler)


def send_email_from_queue(email_id: str):
    print("sending email ", email_id)
    pass


def start_server():
    SERVER_ADDRESS.unlink(missing_ok=True)

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        print(f"Starting up on {SERVER_ADDRESS.name}")
        s.bind(SERVER_ADDRESS.name)
        s.listen(1)
        while True:
            connection, _ = s.accept()
            try:
                while True:
                    data = connection.recv(256)

                    if data:
                        connection.sendall(data)
                    else:
                        break

            finally:
                connection.close()


if __name__ == "__main__":
    start_server()
