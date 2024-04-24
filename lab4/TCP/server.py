import socket
import threading
from typing import List

from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

KEY_SIZE = 2048


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=KEY_SIZE,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def decrypt_message(encrypted_message, private_key):
    original_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return original_message


SERVER_PRIVATE_KEY, SERVER_PUBLIC_KEY = generate_keys()

with open("server_public_key.pem", "wb") as file:
    file.write(
        SERVER_PUBLIC_KEY.public_bytes(
            encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo
        )
    )

SERVER_HOST = ""
SERVER_PORT = 5005

lock = threading.Lock()
barier = threading.Barrier(3)
wiersz: List[str] = []


def handle_client(conn, addr):
    while True:
        data = conn.recv(KEY_SIZE // 8)
        if data:
            with lock:
                decrypted_msg = decrypt_message(data, SERVER_PRIVATE_KEY)
                wiersz.append(decrypted_msg.decode("utf-8"))
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
