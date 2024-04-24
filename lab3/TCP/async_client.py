import asyncio
import random
from typing import List

HOST = "localhost"
PORT = 5005  # The same port as used by the server

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
chunks = [
    [wiersz_array_indexed[i] for i in range(k, len(wiersz_array_indexed), 3)]
    for k in range(3)
]


async def tcp_echo_client(message):
    _, writer = await asyncio.open_connection(HOST, PORT)

    for pair in message:
        writer.write(f"|{pair}".encode("utf-8"))

    print("Closing the connection")
    writer.close()
    await writer.wait_closed()


for chunk in chunks:
    asyncio.run(tcp_echo_client(chunk))
