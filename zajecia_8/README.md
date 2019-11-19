Zajęcia 8
---------

## Pobranie materiałów

```bash
$ git pull
```


## Zapowiedź kartkówek

Ponieważ potrzebują Państwo punktów, każde kolejne zajęcia rozpoczynać
będziemy kartkówką.


## Jaki tryb pracy?

- Tak jak dotychczas?

- Więcej zadań i ciekawostek na ćwiczeniach + zagadnienia do samodzielnego
  przerobienia?

- Najpierw "wykład", później kilka zadań.


## Praca domowa

Jak obliczać dwumian Newtona ze wzoru?

Czy wspominałem ostatnio o programowaniu dynamicznym?


```python
def test(N):
    def newton(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return newton(n-1, k-1) + newton(n-1, k)

    for i in range(0, N) :
        for a in range(0, i+1) :
            print(newton(i, a), end = " ")
        print("\n")

print(newton(10, 5))
```

### Przestrzenie nazw

```python
res = 14

def f(x):
    res = x * x
    return res

print(res)
print(f(2))
print(res)
```

```python
value = 4

def g(x):
    print(value)
    value = 2 * x
    return value

print(g(14))
```

Python to nie JavaScript. ;)

```python
def g(x):
    global value
    print(value)
    value = 2 * x
    return value

print(g(14))
print(value)
```

```python
def g(x):
    print(value)
    global value
    value = 2 * x
    return value
```


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


### Jeszcze raz o list/dict/set comprehension

```python
parzyste = [i for i in range(100) if i % 2 == 0]
```

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

**Na marginesie:**
```python
print('1,2,3'.split(',2,'))
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


Jak policzyć wszystkie odwołania do Nortona?

```python
n = 0
for word in words:
    if word.upper().startswith('NORTON'):
        n += 1
```

Inne (podobne) metody: `.lower()`, `.capitalize()`.

Jak wypisać ponumerowane linie wiersza?

```python
for element in enumerate([3, 1, 4, 1, 5, 9]):
    print(element)
```

```python
for i, line in enumerate(lines, start=1):
    print(i, line, sep='\t')
```

Inny sposób:

```python
with open('reduta.txt', 'r') as fh:
    for i, line in enumerate(fh, start=1):
         print(i, line, sep='\t')
```

Dlaczego to wygląda inaczej?

```python
with open('reduta.txt', 'r') as fh:
    for line in fh:
        print(repr(line))
```

Spróbujmy:

```python
with open('reduta.txt', 'r') as fh:
    for i, line in enumerate(fh, start=1):
        print(i, line.strip(), sep='\t')
```

[W dokumentacji znajdą Państwo więcej metod typu tekstowego](
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
i nie tylko.


## Domyślne wartości argumentów

Zamiast `open('reduta.txt', 'r')` możemy napisać `open('reduta.txt')`.
Podobnie, zamiast `enumerate(iterable, start=0)` możemy napisać
`enumerate(iterable)`.  Dzieje się tak dzięki _domyślnym wartościom
argumentów_.


```python
def add(a, b=1):
    return a + b

print(add(1, 2))
print(add(10)))
print(add(a=100))
print(add(b=42, a=16))
print(add(b=123))
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

### Zadanie 1

Popraw funkcję `append_one()` tak, by jej zachowanie zależało tylko od
wartości argumentów, z jakimi została wywołana.

Podpowiedź: użyj wartości domyślnej `None` i instrukcji warunkowej.


## Wracamy do plików tekstowych

Dlaczego to nie działa?

```python
with open('cp1250.txt') as fh:
    print(fh.read())
```

```python
print(ord('A'))
```

```python
with open('cp1250.txt', 'rb') as fh:
    raw_data = fh.read()
    for n in raw_data:
        print(n)
```

```python
with open('reduta.txt', 'rb') as fh:
    part = fh.read(10)
    for n in part:
        print(chr(n), n)
```

```python
with open('cp1250.txt', 'rb') as fh:
    raw_data = fh.read()
    for n in raw_data:
        print(repr(chr(n)), n)
```

Ten plik ma niestandardowe kodowanie (inne niż [UTF-8](
https://pl.wikipedia.org/wiki/UTF-8).

```python
print(raw_data.decode('cp1250'))
print('można też w drugą stronę'.encode('utf-8'))
```

Aby go wczytać w trybie tekstowym, musimy podać, jakie jest to kodowanie:
```python
with open('cp1250.txt', encoding='cp1250') as fh:
    print(fh.read())
```

Jak powstały te plik?

```python
with open('iso8859_2.txt', mode='w', encoding='iso8859_2') as fh:
    fh.write("Zażółć\ngęślą\njaźń\n")
```

Jeśli pomylimy kodowanie:

```python
with open('iso8859_2.txt', encoding='cp1250') as fh:
    print(fh.read())
```

Tradycyjnie już:
```python
help(open)
```

## Zadanie 2

Zdefiniuj funkcję `make_enumerated_copy(src, dst)` wczytującą
(linia po linii) plik `src` i zapisującą tę linię do pliku `dst`
poprzedzoną trzycyfrowym numerem linii (uzupełnionym zerami w razie
potrzeby, tzn zamiast "1" powinno być "001").

Przyjmij, że `src` i `dst` są już otwarte.

Podpowiedź: uzyj metody `.format()`.


## Zadanie 3

Zdefiniuj funkcję `enumerate_input()` wczytującą kolejne linie znaków
wprowadzonych z klawiatury i wypisujacą je na ekranie wraz z trzycyfrowym
numerem linii (podobnie jak w zadaniu 2).


```python
import sys
from zadanie_02 import make_enumerated_copy
# from rozwiazanie_02 import make_enumerated_copy
make_enumerated_copy(sys.stdin, sys.stderr)
```

## Zadanie 4

Bazując na funkcji `make_enumerated_copy(src, dst)` będącej rozwiązaniem
zadania 2 (samodzielnym lub dostarczonym jako materiał ćwiczeniowy) popraw
program przykładowy program tak, by:
- wywołany z dwoma argumentami będzie zachowywać się jak rozwiązanie
  zadania 2,
- wywołany z jednym argumentem jako `dst` użyje wyjścia standardowego,
- wywołany bez argumentów wypisze kolejne liczby od 0 do 20.


**Pokazać potoki i przekierowania**
Jeśli zostanie czas - zadania 3-5 i 7 z poprzednich zajęć.
