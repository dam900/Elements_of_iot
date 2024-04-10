import socket
import sys
import random
import threading
from typing import List

HOST = 'localhost'
PORT = 5005           # The same port as used by the server

wiersz: str = """Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(— Gdy od płaczącej matki, pod Twoją opiekę
Ofiarowany martwą podniosłem powiekę;
I zaraz mogłem pieszo, do Twych świątyń progu
Iść za wrócone życie podziękować Bogu —)
Tak nas powrócisz cudem na Ojczyzny łono!...
Tymczasem, przenoś moją duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane jakby wstęgą, miedzą
Zieloną, na niej zrzadka ciche grusze siedzą. 
"""

wiersz_array = wiersz.replace("\n", " ").split(" ")
wiersz_array_indexed = [(i, wiersz_array[i]) for i in range(len(wiersz_array))]
random.shuffle(wiersz_array_indexed)

chunk_size = len(wiersz_array_indexed) // 3
chunks = [ [wiersz_array_indexed[i] for i in range(k, len(wiersz_array_indexed), 3)] for k in range(3)]

def send_chunk(chunk: List[str]):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for pair in chunk:
            s.sendall(bytes(str(f"|{pair}"), "utf-8"))

if __name__ == "__main__":
    threads = []
    for chunk in chunks:
        t = threading.Thread(target=send_chunk, args=(chunk,))
        threads.append(t)
        t.start()
        print("Thread started: ", chunks.index(chunk))
    print("All threads started")
    for t in threads:
        t.join()
    print("All threads finished")