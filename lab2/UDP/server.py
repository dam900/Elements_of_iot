import socket
import time

SERVER_HOST = ''
SERVER_PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((SERVER_HOST, SERVER_PORT))
    
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break
        end = time.time()
        print(f"Time taken: {end:.10f}")