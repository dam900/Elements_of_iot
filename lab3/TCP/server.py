import socket
import threading
from typing import List

SERVER_HOST = ""
SERVER_PORT = 5005

lock = threading.Lock()
barier = threading.Barrier(3)
wiersz: List[str] = []


def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if data:
            with lock:
                wiersz.append(data.decode("utf-8"))
        if not data:
            break
    conn.close()
    barier.wait()


threads = []
run = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((SERVER_HOST, SERVER_PORT))

    while run:
        sock.listen()

        conn, addr = sock.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
        threads.append(t)
        if len(threads) == 3:
            run = False
    for thread in threads:
        thread.join()
    print("All threads finished")
    wiersz = [x for x in "".join(wiersz).split("|") if x != ""]
    wiersz = list(
        map(lambda x: x.replace("(", "").replace(")", "").strip().split(","), wiersz)
    )
    wiersz = map(lambda x: (int(x[0]), x[1].strip().replace("'", "")), wiersz)
    wiersz = sorted(wiersz, key=lambda x: x[0])
    print(" ".join(map(lambda x: x[1], wiersz)))
