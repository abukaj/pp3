Zajęcia 4
-----------

## Zapowiedź kartkówki

Na następnych ćwiczeniach odbędzie się kartkówka (krótkie zadanie
programistyczne) z zajęć 1-4.  W związku z tym proszę Państwa o:
1. Upewnienie się, czy zagadnienia wymienione w odpowiednich punktach
[orientacyjnego programu zajęć](
https://brain.fuw.edu.pl/edu/index.php/%22Programowanie_z_Pythonem3%22)
są dla Państwa jasne.  Jeśli chcieliby Państwo, żeby jakieś zagadnienie
zostało ponownie omówione, proszę o przesłanie stosownej wiadomości na
adres: j.kowalski@nencki.gov.pl.  Układając zadanie postaram się omijać
niejasne dla Państwa tematy, które postaram sie powtórzyć po kartkówce.
Proszę, żeby wiadomości przesłali państwo **do piątku 25 października**
(zadanie będę układać w sobotę i wiadomości które otrzymam później mogą
nie zostać uwzględnione).
2. Jeśli coś na dzisiejszych zajęciach będzie dla Państwa niejasne,
**proszę pytać**.  Rzeczy, które pojawią się na dzisiejszych zajęciach,
uznam za opanowane przez Państwa niezależnie od otrzymanych wiadomości.
3. Upewnienie się, że są Państwo w stanie wysłać z pracowni e-mail
z załącznikiem.  Wysłanie wiadomości z rozwiązaniem będzie kluczowym
elementem zadania. ;)



## Na rozgrzewkę

```python
>>> help(print)
>>> print(print.__doc__)
>>> print(type(print.__doc__))
>>> print(1_000_000 == 1_000_000)
>>> print(1_000_000 is 1_000_000)
>>> a = 1
>>> b = 1
>>> print(a is b)
>>> a = 1_000_000
>>> b = 1_000_000
>>> print(a is b)
>>> print(id(a))
>>> print(id(b))
```


## Iteracja
```python
for i in [1, 2, 3]:
    print(i)
```

```python
for i in range(100):
    print(i)
```

```python
for i in range(98, 100):
    print(i)
```

```python
for i in range(3, 100, 10):
    print(i)
```
### Wcięcia

W języku Python **wcięcia są istotne**.  Nie tylko zwiększają
**czytelność**, ale również określają **strukturę** programu.
Wcięcia wykonujemy używając znaków odstępu (tzw. "spacji").
Niektórzy używają znaku tabulacji (osobiście nie rekomenduję).
**Użycie mieszanki znaków odstępu i tabulacji jest proszeniem
się o kłopoty** - będzie oceniane jako błąd.



## Typ logiczny

```python
>>> a = 1 == 2
>>> print(a)
>>> print(type(a))
>>> print(bool(0))
>>> print(bool(1))
>>> print(bool(10))
>>> print(bool(''))
>>> print(bool('abc'))
```


## Zadanie 1

Zdefiniuj funkcję `even(n)` (ang. parzysty/a).


## Instrukcja warunkowa

```python
a = True
if a:
    print('Prawda')
```

```python
a = False
if a:
    print('Prawda')
```

```python
a = False
if a:
    print('Prawda')
else:
    print('NIEPRAWDA!!!')
```


## Zadanie 2(a,b)

Dla liczb z przedziału 1-10 wypisz wszystkie parzyste korzystając
(lub nie) z funkcji `even()`.


## Zadanie 3(a,b)

Dla liczb z przedziału 1-10 wypisz wszystkie nieparzyste korzystając
(lub nie) z funkcji `even()`.


## Zadanie 4

Zdefiniuj funkcję `factorial(n)` (ang. silnia).


## Zadanie 5

Oblicz `factorial(1_000_000)`.


## "Instrukcja wyboru"

Teoretycznie nie występuje w języku Python, ale mamy odpowiadającą jej
"drabinkę `elif`-ów".

```python
if a == 0:
    print('zero')
elif a == 1:
    print('jeden')
elif a == 2:
    print('dwa')
else:
    print('inny przypadek')
```

Czasem uznaje się ją za tzw. ["zapach kodu"](
https://pl.wikipedia.org/wiki/Zapachy_kodu) - może wskazywać na niewłaściwy
sposób napisania programu.  Osobiście sugeruję rozważenie innych rozwiązań
gdy sa dostępne.

```python
polish_numbers = {0: 'zero',
                  1: 'jeden',
                  2: 'dwa',
                  }
print(polish_numbers.get(a, 'inny przypadek')
```


## Wyrażenie warunkowe

```python
temperature = 160
water = 'liquid' if temperature > 0 else 'solid'
print(water)
```

Wyrażenia warunkowe można zagnieżdżać.

```python
temperature = -273
water = 'liquid' if temperature < 100 else 'gas' if temperature > 0 else 'solid'
print(water)
```


## Zadanie 5

Popraw ostatni przykład tak, aby był (z grubsza) zgodny z fizyką (przy ciśnieniu 1 atm).
```python
temperature = -273
# water = 'liquid' if temperature < 100 else 'gas' if temperature > 0 else 'solid'
water = 'liquid' if temperature < 100 else 'gas' if temperature > 0 else 'solid'
print(water)
```


## Zadanie 6

Zdefiniuj funkcję `pairity(n)` (ang. "parzystość") zwracającą `'even'`
dla parzystego `n` i `'odd'` dla nieparzystego.


## Zadanie 7

Dla liczb od 0 do 10 **włącznie** wypisz: liczbę i jej parzystość rozdzielone
znakiem tabulacji (`'\t'`).

[Metoda pozwalająca wykorzystać obiekt tekstowy jako szablon](
https://docs.python.org/3/library/stdtypes.html#str.format).
