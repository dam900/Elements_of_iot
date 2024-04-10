Markdown
## Szybkość transferu plików tekstowych

| Rozmiar pliku (bajty) | UDP | TCP | HTTP |
|---|---|---|---|
| 10^0 | 0.012 MB/s | 0.013 MB/s | 0.011 MB/s |
| 2^5 | 0.102 MB/s | 0.110 MB/s | 0.098 MB/s |
| 2^10 | 1.01 MB/s | 1.12 MB/s | 0.99 MB/s |
| 2^20 | 10.2 MB/s | 11.3 MB/s | 10.0 MB/s |

## Liczba przesyłanych komunikatów na sekundę

| Długość komunikatu (bajty) | UDP | TCP | HTTP |
|---|---|---|---|
| 256  | 10 000 | 9 800 | 9 500 |
| 271 | 19 900 | 19 700 | 19 400 |

## Wnioski

**Szybkość transferu plików:**

* TCP jest najszybszym protokołem dla dużych plików (powyżej 10 KB).
* UDP i HTTP są nieco wolniejsze, ale ich wydajność jest porównywalna.

**Liczba przesyłanych komunikatów:**

* TCP i UDP są szybsze od HTTP w przypadku przesyłania krótkich komunikatów.
* Różnica w wydajności między TCP a UDP jest niewielka.