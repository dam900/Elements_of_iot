import socket
import sys
import utils

HOST = 'localhost'
PORT = 5005           # The same port as used by the server

if __name__ == "__main__":
    file_size: int = int(sys.argv[1])
    file_name: str = utils.generate_file(file_size)
    with open(file_name, "rb") as f:    
        file_bytes = f.read()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(file_bytes)
    utils.remove_file(file_name)
