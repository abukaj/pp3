Zajęcia 8
---------

## Pobranie materiałów

```bash
$ git pull
```


## Zapowiedź kartkówek

Ponieważ potrzebują Państwo punktów, każde kolejne zajęcia rozpoczynać
będziemy kartkówką.


## Z poprzednich zajęć


### Kilka przydatnych funkcji

```python
numbers = [3, 1, 4, 1, 5, 9]

print(sorted(numbers))
print(numbers)
numbers_sorted = sorted(numbers, reverse=True)
print(numbers_sorted)

numbers_sorted.sort()
print(numbers_sorted)

print(numbers)

for i in reversed(numbers):
    print(i)
```

Niektóre funkcje (i metoda) mają więcej możliwości - zachęcam do
używania funkcji `help()` oraz czytania [dokumentacji](
https://docs.python.org/3/library/functions.html#built-in-funcs).


### Jak ponumerować iterowane elementy?

```python
numbers = [10, -20, 40]
for i, n in enumerate(numbers):
    print('{}\t{}'.format(i, n))
```

```python
mapping = dict(enumerate('abcdefghijklmnopqrstuvwxyz', start=1))
```

## Poranek poetycko-historyczny

Otwórzmy do odczytu plik 'reduta.txt' i wczytajmy jego zawartość:

```python
fh = open('reduta.txt', 'r')
text = fh.read()
print(text)
```

Zwróćmy uwagę, że ponowna próba wczytania zawartości się nie powiedzie:

```python
print(fh.read())
```

W "dawnych czasach" dane przechowywane były na taśmach (perforowanych,
magnetycznych, itp.), które odczytywano sekwencyjnie.  Aby wczytac dane
ponownie, trzeba było tasmę przewinąć (ustawić głowicę odczytującą na
początku tasmy).  Pliki odziedziczyły to rozwiązanie, zatem "przewińmy"
nasz plik:

```python
fh.seek(0)
print(fh.read())
```

Po skończonej pracy naleźy po sobie posprzątać - w tym przypadku
zamknąć otwarty plik:

```python
fh.close()
```

Możemy też usunąć etykietę `fh`:
```python
del fh
```
co pozwoli interpreterowi na zwolnienie pamięci zajmowanej przez zbędny
już obiekt.  Jeśli etykieta była zdefiniowana w funkcji, jest ona
usuwana automatycznie po prawidłowym opuszczeniu funkcji.

Pamiętanie o tym bywa kłopotliwe.  Na szczęście obiekt zwracany przez
funkcję `open()` jest zarządcą kontekstu (ang. "context manager";
obiekt posiadający metody `.__enter__()` i `.__exit__()`) i może nas
w tym wyręczyć, gdy tylko przestanie nam być potrzebny:

```python
with open('reduta.txt', 'r') as fh:
    text = fh.read()
    print(fh.closed)

print(fh.closed)
```

Policzmy słowa w wierszu:
```python
words = text.split()
print(len(words))
```

Jak policzyć linie?

```python
lines = text.split('\n')
print(len(lines))
```

Ale to nie może być aż takie proste:
```python
print(words[24])
print(lines[-1])
```

Słowem jest dowolny niepusty ciąg _czarnych znaków_, linia zaś może być
pusta.  Ze względów historycznych linie mogą być rozdzielone znakami
nowej linii (`'\n'`;
[LF](https://en.wikipedia.org/w/index.php?title=Line_feed&redirect=no);
ang. "Line Feed"), znakami powrotu karetki (`'\r'`;
[CR](https://en.wikipedia.org/wiki/Carriage_return),
ang. "Carriage Return") bądź obydwoma (`\r\n` lub `\n\r`).  Ograniczamy
się tu wyłącznie do kodowania tekstu w sposób zgodny z [ASCII](
https://en.wikipedia.org/wiki/ASCII).  Standardowo dziedzice systemu
Unix (choćby pochodzące z "nieprawego łoża", jak Linux) używają znaków
_LF_, zaś systemu DOS - _CRLF_.


```python
print('1,2,3'.split(',2,'))
```

**TODO**


## Domyślne argumenty

```python
def add(a, b=1):
    return a + b
```

Co tu się dzieje?
```python
def append_one(numbers=[]):
    numbers.append(1)
    return numbers

print(append_one([0]))
numbers = append_one()
print(numbers)
print(append_one())
print(append_one([]))
print(numbers is append_one())
print(numbers is append_one([]))
```

## Zadanie 2

Popraw funkcję `append_one()` tak, by jej zachowanie zależało tylko od
wartości argumentów, z jakimi została wywołana.

Podpowiedź: użyj wartości domyślnej `None` i instrukcji warunkowej.


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
for something in zip([1, 2, 3], [10, 20, 30], [100, 200, 300]):
    print(something)
```


### Zadanie 4

Przepisz funkcję `multiply(A, B)` korzystając z funkcji `zip()`.

Co się dzieje, gdy `len(A) != len(B)`?


## Jeszcze raz o list/dict/set comprehension

```python
parzyste = [i for i in range(100) if i % 2 == 0]
```


## Zadanie 5

Uzupełnij funkcję `primes_up_to(n)` tak, by zwracała zbiór wszystkich liczb
pierwszych nie większych niż `n`.


## Zadanie 6 - dla chętnych

Uzupełnij funkcję `sieve_of_eratosthenes(n)` tak, by implementowała
[sito Eratostenesa](https://pl.wikipedia.org/wiki/Sito_Eratostenesa).


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

