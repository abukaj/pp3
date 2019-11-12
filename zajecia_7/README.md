Zajęcia 7
---------

### Pobranie materiałów

```bash
$ git pull
```


## Z poprzednich zajęć

Zadania 8-11.


## Omówienie zadań domowych


## Zadanie 1

Zdefiniuj funkcję `wait_for_password(password)` która będzie pytać
użytkownika o hasło tak długo, aż ten wpisze poprawne (tzn. podane
jako parametr) - wtedy funkcja zakończy swoje działanie.


## Symulowanie pętli for pętlą while

```python
i = 0
numbers = [3, 1, 4, 1, 5, 9]
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
mapping2['cztery'] = 4
print(mapping2)
print(mapping)

mapping2 = dict(mapping)
```


## Jak ponumerować obiekty uzywając pętli for?

```python
numbers = [10, -20, 40]
for i, n in enumerate(numbers):
    print('{}\t{}'.format(i, n))
```


## Zadanie 2

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


## Zadanie 3

Przepisz funkcję `multiply(A, B)` korzystając z funkcji `zip()`.

### Sito Erastostenesa
