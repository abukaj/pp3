Zajęcia 7
---------

## Pobranie materiałów

```bash
$ git pull
```


## Z poprzednich zajęć

Zadania 8-11.


## Omówienie zadań domowych


## Zadanie 1

Popraw funkcję `wait_for_password(password)` by pytała użytkownika
o hasło tak długo, aż ten wpisze poprawne (tzn. podane jako parametr)
- i wtedy kończyła swoje działanie.

Są na to przynajmniej 3 podobnie eleganckie sposoby.


## Symulowanie pętli for pętlą while

```python
numbers = [3, 1, 4, 1, 5, 9]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```


### Po co nam petla for?

#### Zbiory
```python
{1}
{1, 2, 3}
set(range(3))
set()

a = set()
a.add(12)
print(a)
print(12 in a)
a.remove(12)
print(a)

{1, 2} | {2, 3}
{1, 2} & {2, 3}
{1, 2} ^ {2, 3}

{i ** 2 - 2 * i + 1 for i in range(4)}
```

#### Krotki

```python
(1, 2)
(1, 2, 3)
()
(1)
(1,)
1,
1, 2, 3
(1, 2) + (3, 4)
(1, 2) * 4
```


#### Frozenset

```python
frozenset([1, 2, 3])
```


#### Słowniki

```python
{1: 'jeden', 2: 'dwa'}
type({})
{'lista': []}
{[]: 'lista'}
{(): 'krotka'}
dict()
dict(jeden=1)

mapping = dict([(1, 'a'),
                (2, 'b')])
for number in mapping:
    print(number)


print(list(mapping))
print(list(mapping.keys())

for letter in mapping.values():
    print(letter)

print(list(mapping.values()))

for number, letter in mapping.items():
    print(number, letter)

print(1 in mapping)
print(mapping[1])
print(mapping[3])
print(mapping.get(3))
print(mapping.get(3, 'Nie ma. :-('))
mapping[3] = 'c'
print(mapping)

mapping.update([(1, 'A'), (3, 'C')])
print(mapping)

mapping.update(cztery=4)
print(mapping)

mapping2 = mapping
del mapping2['cztery']
print(mapping2)
print(mapping)

mapping2 = mapping.copy()
mapping2[4] = 'd'
print(mapping2)
print(mapping)

mapping2 = dict(mapping)

{'{} ** 2'.format(i): i for i in range(4)}
```


## Kilka przydatnych funkcji

```python
numbers = [3, 1, 4, 1, 5, 9]
print(max(numbers))
print(max(1, 2))

print(min(numbers))
print(min(1, 2))

print(sorted(numbers))
print(numbers)
numbers_sorted = sorted(numbers, reverse=True)
print(numbers_sorted)

numbers_sorted.sort()
print(numbers_sorted)

for i in reversed(numbers):
    print(i)

print(sum(numbers))
sum([[1], [2], [3]])
print(sum([[1], [2], [3]], []))
print(sum([[1], [2], [3]], [1337]))

strings = list(map(str, numbers))
print(strings)

sum(strings, '')
print(''.join(strings))

pi = float(''.join(strings))
print(pi)
print(round(pi))

print(abs(-3))
```

Niektóre funkcje (i metoda) mają więcej możliwości - zachęcam do
używania funkcji `help()` oraz czytania [dokumentacji](
https://docs.python.org/3/library/functions.html#built-in-funcs).


## Jak ponumerować iterowane elementy?

```python
numbers = [10, -20, 40]
for i, n in enumerate(numbers, start=1):
    print('{}\t{}'.format(i, n))
```

```python
mapping = dict(enumerate('abcdefghijklmnopqrstuvwxyz', start=1))
```


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
for something in zip([1, 2, 3], [4, 5], [6, 7, 8]):
    print(something)
```


## Zadanie 4

Przepisz funkcję `multiply(A, B)` korzystając z funkcji `zip()`.

Co się dzieje, gdy `len(A) != len(B)`?


## Jeszcze raz o list/dict/set comprehension

```python
parzyste = [i for i in range(100) if i % 2 == 0]
```


## Zadanie 5

Uzupełnij funkcję `primes_up_to(n)` tak, by zwracała zbiór wszystkich liczb
pierwszych nie większych niż `n`.


## Zadanie 6

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

