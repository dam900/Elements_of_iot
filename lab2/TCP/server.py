import socket
import time

SERVER_HOST = ''
SERVER_PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((SERVER_HOST, SERVER_PORT))
    
    while True:
        sock.listen(1)
        conn, addr = sock.accept()
        
        with conn:
            start = time.time()
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            end = time.time()
            print("Time taken: ", end-start)