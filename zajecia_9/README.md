Zajęcia 8
---------

## Pobranie materiałów

```bash
$ git pull
```


## Jaki tryb pracy? Odpowiedź.

- Tak jak dotychczas?

- Więcej zadań i ciekawostek na ćwiczeniach + zagadnienia do samodzielnego
  przerobienia?

- Najpierw "wykład", później kilka zadań.


## Kartkówka

Uzupełnij szablon "kartkowka2.py" wpisując swój numer albumu oraz
definiując we wskazanym miejscu funkcję `inverted()` zwracającą
"odwrócony" słownik `d` (objaśnienie na tablicy)


### Przesłanie rozwiązania

Plik "kartkowka2.py" zawierający rozwiązanie zadania należy przesłać
jako załącznik wiadomości e-mail zatytułowanej "Kartkówka 2" na dwa
adresy e-mail:
 - kartkowka20191126@amix.org.pl
 - j.m.dzik@nencki.edu.pl

**Proszę sprawdzić pred wysłaniem, czy próba uruchomienia programu
nie kończy się błędem składni**

## Kolokwium

### Zad. 1 - testy

```python
assert nwd(123, 123) == 123
assert nwd(4, 2) == 2
assert nwd(2, 4) == 2
assert nwd(63, 17) == 1
```

### Zad. 1 - algorytm Euklidesa

```python
def nwd(a, b):
    # tego przypadku często brakowało
    if a < b: 
        return nwd(b, a)

    assert a >= b

    r = a % b

    if r == 0:
        return b

    return nwd(b, r)
```


### Zad. 1 - algorytm naiwny

```python
def factors(n):
    return {i for i in range(n + 1) # włącznie z n
            if n % i == 0}

def nwd(a, b):
    return max(factors(a) ^ factors(b))
```

### Zad. 2 - na tablicy

Algorytm:
1. numer jest ciągiem cyfr dziesiętnych
1a. numerujemy je od końca (ostatnia: 1, przedostatnia: 2, itd.)
2. cyfry o numerach nieparzystych mnożymy przez 2, a o parzystych przez 1
3. jeśli w wyniku mnożenia otrzymano liczbę dwucyfrową, dodaje się cyfry
   do siebie otrzymując liczbę jednocyfrową
4. dodaje się wszystkie otrzymane liczby do siebie
5. z wyniku bierze się jedynie cyfrę jedności
6. jeżeli rezultatem nie jest 0, numer nie jest poprawny.
```


## Moduły

Znamy polecenie `import sys`.  Po jego wykonaniu uzyskamy dostęp do
obiektów z przestrzeni nazw modułu `sys`:

```python
import sys

print(sys.argv)
print(sys.version)
print(sys.version_info)
```

Jak sprawdzić, jakie to nazwy?  Zaimportowany moduł też jest obiektem,
którego atrybutami są obiekty z jego przestrzeni nazw.  Funkcję `dir()`
znamy:

```python
print(dir(sys))
```

Gdy potrzebujemy dostępu do tylko jednego (lub kilku) obiektów modułu,
możemy je przenieść bezpośrednio do naszej przestrzeni nazw,
nie korzystając przy tym z pośrednictwa obiektu modułu:

```python
from math import pi
print(pi)
```

lub

```python
from math import floor, ceil
print(floor(12.9), ceil(12.9))
```

Nazwa modułu lub obiektu nie zawsze musi nam się podobać.  Na szczęście
w naszej przestrzeni nazw można je zmienić:
```python
import numpy as np
from math import sqrt as pierwiastek_kwadratowy
```


Możecie spotkac się też z taką konstrukcją:
```python
from sys import *
```

Przenosi ona do naszej przestrzeni nazw wszystkie "publiczne" obiekty
danego modułu.  Jest ona o tyle niebezpieczna, że może nam ona nadpisać
nazwy istniejące:

```python
version = 4
from sys import *
print(version)
```
Konstrukcja ta również może nam zaśmiecić przestrzeń nazw, zwłaszcza gdy
moduł zawiera wiele zbędnych nam "publicznych" obiektów.  Nalezy jej
unikać w kodzie programu, w trybie interaktywnym zaś - wedle Państwa
uznania.


Moduły moga być połączone w większe paczki:

```python
import os.path
print(os.path.join('katalog', 'plik.txt'))
import os
print(dir(os))
```

### Gdzie fizycznie znajdują się moduły zanim zostaną zaimportowane?

W katalogach z modułami.  Mamy tam bibliotekę standardową (moduły
dostępne w każdej instalacji języka Python) oraz dodatkowo zainstalowane
pakiety.  Ale możemy również importowac moduły znajdujące się w katalogu
roboczym:

```python
import modul
```

```bash
python3 modul.py
```

**Omówić kod modułu**

**Powiedzieć, co robi `sys.stderr`.**

#### Jak (po raz kolejny) mozna strzelić sobie w stopę?

```bash
touch numpy.py
```

```python
from numpy import array
import numpy
print(dir(numpy))
```


## Zadanie 1

Na poprzednich zajęciach zdefiniowaliśmy funkcję
`make_enumerated_copy(src, dst)`.  Znajduje się ona w pliku "modul.py".

Uzupełnij program tak, by ją wykorzystał.


## Przekierowania

```bash
python3 zadanie_01.py
python3 zadanie_01.py README.md
python3 zadanie_01.py < README.md
python3 zadanie_01.py modul.py
python3 zadanie_01.py modul.py > zadanie_01_stdout.txt
head zadanie_01_stdout.txt
python3 zadanie_01.py modul.py 2> zadanie_01_stderr.txt
head zadanie_01_stderr.txt
python3 zadanie_01.py < README.md > zadanie_01_stdout.txt 2> zadanie_01_stderr.txt
head zadanie_01_stdout.txt
head zadanie_01_stderr.txt
```

## Zadanie 2

Uzupełnij program tak, by kopiował plik zamieniając małe litery na wielkie.


```bash
python3 zadanie_02.py ../zajecia_8/reduta.txt
python3 zadanie_02.py
```


## Potoki

A co by było, gdyby podpiąć wyjście jednego programu jako wejście drugiego?

```bash
python3 zadanie_02.py ../zajecia_8/reduta.txt | python3 zadanie_01.py
python3 zadanie_02.py ../zajecia_8/reduta.txt | python3 zadanie_01.py | grep NORTON
python3 zadanie_02.py ../zajecia_8/reduta.txt | python3 zadanie_01.py | grep NORTON | python3 zadanie_01.py
```

## Z poprzednich zajęć


## Zadanie 3

Zdefiniuj (nie korzystając z `zip()`) funkcję `multiply(A, B)`
zwracającą nową listę, której elementy będą iloczynem odpowiednich
elementów list A i B.  Załóż, że listy są równej długości.


## Funkcja `zip()`

```python
for a, b in zip([1, 2, 3], [4, 5, 6]):
    print(a, b)
```

```python
for something in zip([1, 2, 3], [4, 5], [6, 7, 8]):
    print(something)
```


## Zadanie 4

Przepisz funkcję `multiply(A, B)` korzystając z funkcji `zip()`.

Co się dzieje, gdy `len(A) != len(B)`?



## Zadanie 5

Uzupełnij funkcję `primes_up_to(n)` tak, by zwracała zbiór wszystkich liczb
pierwszych nie większych niż `n`.


## Zadanie 6

Zdefiniuj funkcję `python_2_map(f, iterable)`, która zwróci listę
wartości funkcji `f(x)` dla kolejnych `x` w `iterable`.



## Zadanie 7

Uzupełnij funkcję `insertion_sort(sequence)` tak, aby implementowała
w miejscu algorytm sortowania przez wstawianie.

### Proste algorytmy sortowania w miejscu

* [Sortowanie przez wstawianie](
    https://pl.wikipedia.org/wiki/Sortowanie_przez_wstawianie).
* [Sortowanie przez wybieranie](
    https://pl.wikipedia.org/wiki/Sortowanie_przez_wybieranie).
* [Sortowanie bąbelkowe](
    https://pl.wikipedia.org/wiki/Sortowanie_b%C4%85belkowe).



## Zadanie 8

Uzupełnij funkcję `sieve_of_eratosthenes(n)` tak, by implementowała
[sito Eratostenesa](https://pl.wikipedia.org/wiki/Sito_Eratostenesa).

