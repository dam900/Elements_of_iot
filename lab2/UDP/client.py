import socket
import sys
import utils

HOST = 'localhost'
PORT = 5005           # The same port as used by the server

if __name__ == "__main__":
    file_size: int = int(sys.argv[1])
    file_name: str = utils.generate_file(file_size)
    with open(file_name, "rb") as file:    
        file_bytes = file.read()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((HOST, PORT))
            s.sendall(file_bytes)
            data = s.recv(1024)
        print('Received', repr(data))
    utils.remove_file(file_name)