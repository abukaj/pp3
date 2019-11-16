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

