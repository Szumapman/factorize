# Zadanie domowe # 3 (Moduł 2 web)

## Druga część dot. procesów

Zaimplementuj funkcję factorize, która przyjmuje listę liczb, po czym zwraca listę liczb, przez które liczby z listy wejściowej są podzielne bez reszty.

Zaimplementuj wersję synchroniczną i zmierz czas wykonania.

Następnie popraw wydajność swojej funkcji, wykorzystując wiele rdzeni procesora do obliczeń równoległych i ponownie zmierz czas wykonania. W celu ustalenia liczby rdzeni na komputerze, użyj funkcji cpu_count() z pakietu multiprocessing

Poprawność algorytmu samej funkcji można sprawdzić za pomocą testu:

```python
def factorize(*number): 
   # YOUR CODE HERE
   raise NotImplementedError() # Remove after implementation

a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
```
