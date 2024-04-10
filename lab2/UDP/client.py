import socket
import sys
import time
import utils

HOST = 'localhost'
PORT = 5005           # The same port as used by the server

if __name__ == "__main__":
    file_size: int = int(sys.argv[1])
    file_name: str = utils.generate_file(file_size)
    with open(file_name, "rb") as f:    
        file_bytes = f.read()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            start = time.time()
            s.sendto(file_bytes, (HOST, PORT))
            print(f"Time taken: {start:.10f}")
    utils.remove_file(file_name)