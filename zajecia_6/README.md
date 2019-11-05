Zajęcia 6
---------

### Pobranie materiałów

```bash
$ git pull
```


## Wyniki kartkówki

Otrzymałem 10 rozwiązań.  Informację zwrotną odesłałem na indywidualne
adresy e-mail.

Oczekiwane rozwiązanie:

```python
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
```

**Czy są jakieś pytania?**


### Ciekawostka

Wszyscy, którzy skorzystali z zaproponowanych testów (a przynajmniej
je odkomentowali) napisali poprawne rozwiązanie.



## Przydatne do zadania domowego

### Jak napisać skrypt przyjmujący argumenty?

Skrypt wypisujący argumenty, z jakimi został wywołany:

```python
#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    print(sys.argv)

    for value in sys.argv:
        print(value)
```

Jaki jest pierwszy argument (o indeksie 0)?


Skrypt dodający liczby:

```python
#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    result = 0.

    for value in sys.argv[1:]:
        result += float(value)

    print(result)
```

Skrypt odejmujacy dwie liczby:

```python
#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print('Usage: {} <number a> <number b>'.format(sys.argv[0]))

    else:
        print(float(sys.argv[1]) - float(sys.argv[2]))
```

### Jak połączyć listę stringów w jeden string?

```python
>>> strings = ['a', 'b', 'cde', '{}'.format(123), str(3.14)]
>>> combined = 'SEPARATOR'.join(strings)
>>> print(combined)
```


## Z poprzednich zajęć

Przed kolokwium musimy trochę zwiększyć tempo.  Dlatego przeskoczymy
zadania 8-12 i przejdziemy od razu do 13 i 14.  Niestety, pominiemy
kilka ciekawostek, do których spróbujemy powrócić po kolokwium.



## Kilka słów o listach

**Lista (w języku Python) to nie lista.**  Warto o tym pamiętać
czytając książki o klasycznych strukturach danych.

Krótkie tworzymy używając nawiasów kwadratowych:

```python
>>> numbers = [1, 2, 3]
```

Oczywiście listy, jako obiekty, mogą być elementami innych list:
```python
>>> nested_lists = [[], [], []]
```

**Dobrą praktyką jest, by elementy listy były podobnego typu.**
Staramy się unikać list takich jak:
```python
>>> not_recommended = [1, 3.14, 'e', [], ()]
```


Długość listy zwraca nam funkcja `len()`:
```python
>>> numbers = [1, 2, 3]
>>> length = len(numbers)
>>> print(length)
```

Można też bezpośrednio użyć metody specjalnej:
```python
>>> length = numbers.__len__()
>>> print(length)
```

Metoda `.append()` pozwala dodać nowy element na końcu listy:

```python
>>> numbers.append(4)
>>> print(numbers)
```

Czy lista może być elementem samej siebie?

```python
>>> list_that_contains_itself = []
>>> list_that_contains_itself.append(list_that_contains_itself)
>>> print(list_that_contains_itself is list_that_contains_itself[0])
>>> print(list_that_contains_itself)
```


### Zadanie 1

Używając metody `.append()` zdefiniuj funkcję `natural_numbers(n)`
zwracającą listę `n` najmniejszych liczb naturalnych (w kolejności
rosnącej).


#### Jak zrobić to prościej?

Możemy użyć konstruktora `list()`:
```python
def natural_numbers(n):
    return list(range(n))
```


### Zadanie 2

Używając metody `.append()` zdefiniuj funkcję `ones(n)` zwracającą
listę `n` jedynek.


#### Jak zrobić to prościej?

Możemy przemnożyć listę `[1]` przez `n`:

```python
def ones(n):
    return [1] * n
```


### Co się stało?

```python
>>> lists = [[]] * 100
>>> print(lists[1])
>>> lists[0].append(1)
>>> print(lists[0])
>>> print(lists[1])
```


### Zadanie 3

Uzywając metody `.append()` zdefiniuj funkcję `list_of_lists(n)`
zwracającą poprawną listę `n` list.

#### Jak zrobić to prościej?

Używając tzw. _list comprehension_:
```python
def list_of_lists(n):
    return [[] for _ in range(n)]
```


### Zadanie 4

Uzywając metody `.append()` zdefiniuj funkcję `list_of_squares(n)`
zwracającą listę kwadratów kolejnych liczb naturalnych nie większych
niż `n`.

#### Jak zrobić to prościej?

Pnownie _list comprehension_:

```python
def list_of_squares(n):
    return[i**2 for i in range(n)]
```


### Usuwanie elementu z listy.

Sposób klasyczny:
```python
>>> numbers = [1, 2, 3]
>>> del numbers[1]
>>> print(numbers)
```

```python
>>> numbers = [1, 2, 3]
>>> del numbers[-1]
>>> print(numbers)
```

Metoda `pop()`:
```python
>>> numbers = [1, 2, 3]
>>> item = numbers.pop(1)
>>> print(item)
>>> print(numbers)
```

```python
>>> numbers = [1, 2, 3]
>>> item = numbers.pop()
>>> print(item)
>>> print(numbers)
```

### Znajdowanie elementu listy

```python
>>> numbers = [10, 20, 30]
>>> print(10 in numbers)
>>> print(42 in numbers)
>>> print(numbers.index(20))
>>> print(numbers.index(42))
```

```python
>>> numbers = [10, 20, 20]
>>> print(numbers.indes(20))
```


## Dlaczego to nie działa?

```python
>>> numbers = [1, 2, 3]
>>> for x in numbers:
...     x = x + 1
>>> print(numbers)
>>> print(x)
```


## Zadanie 5

Uzywając metody `.append()` zdefiniuj funkcję `increased(items)`
zwracającą nową listę zawierającą powiększone o 1 elementy listy
`items`.


## Zadanie 6

Uzywając list comprehension zdefiniuj funkcję `increased(items)`
zwracającą nową listę zawierającą powiększone o 1 elementy listy
`items`.


## Zadanie 7

Zdefiniuj _działającą w miejscu_ funkcję `increase_every_item(items)`
powiększającą o 1 kazdy element listy `items`.


## Zadanie 8

Zdefiniuj funkcję `factors(n)` zwracającą listę wszystkich dzielników
liczby `n` (włącznie z `n`) w kolejności rosnącej.


## Zadanie 9

Zdefiniuj (korzystając z iteracji zamiast rekursji) funkcję
`harmonic_number(n)` zwracającą `n`-tą [liczbę harmoniczną](
https://pl.wikipedia.org/wiki/Liczby_harmoniczne)
(sumę odwrotności liczb naturalnych od 1 do `n`).


## Zadanie 10

Zdefiniuj (korzystając z pętli `for`) funkcję
`index_of_first_greater_harmonic_number(x)` zwracającą indeks pierwszej
[liczby harmonicznej](https://pl.wikipedia.org/wiki/Liczby_harmoniczne)
większej od `x`.



## Pętla while

Jest to pętla, której ciało jest wykonywane, dopóki jest spełniony
pewien warunek.

```python
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

## Zadanie 11

Przepisz (korzystając z pętli `while`) funkcję
`index_of_first_greater_harmonic_number(x)`.


## Zadanie 12

Zdefiniuj (korzystając z rekursji) funkcję `strange(n, m)`.

```
strange(0, 0) = 1
strange(n + 1, 0) = (n + 1) * strange(n, 0)
strange(0, m + 1) = (m + 1) * strange(n, 0)
strange(n + 1, m + 1) = strange(n + 1, m) - strange(n, m + 1)
```


## Zadanie 13

Zdefiniuj funkcję `decay(m0, t, halflife)` obliczającą, ile
z początkowej masy pierwiastka `m0` o okresie połowicznego zaniku
`halflife` pozostanie po czasie `t`.  Przyjmij, że `halflife` i `t`
sa w tych samych jednostkach.


## Jesli zostanie czas

### Instrukcje break i continue

Instrukcja `break` przerywa wykonanie pętli (całej).  Instrukcja
`continue` przerywa wykonanie aktualnej iteracji ciała petli
i rozpoczyna kolejną iterację.


## Po co nam petla for?

Kilka słów o zbiorach i słownikach.


## Jak ponumerować obiekty uzywając pętli for?

```python
numbers = [10, -20, 40]
for i, n in enumerate(numbers):
    print('{}\t{}'.format(i, n))
```



### Sito Erastostenesa
