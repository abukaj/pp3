Zajęcia 5
---------

## Kartkówka

Uzupełnij szablon "kartkowka1.py" wpisując swój numer albumu oraz
definiując we wskazanym miejscu funkcję `(x)` zwracającą
liczby `x` (definicja na tablicy).


### Pobranie szablonu rozwiązania

```bash
$ git pull
```


### Podpowiedź

Zdefiniowana funkcja powinna przejść następujące testy:
```python
assert == 0
assert == 1
assert == 2
```


### Przesłanie rozwiązania

Plik "kartkowka1.py" zawierający rozwiązanie zadania należy przesłać
jako załącznik wiadomości e-mail zatytułowanej "Kartkówka 1" na dwa
adresy e-mail:
 - kartkowka20191030@amix.org.pl
 - j.kowalski@nencki.gov.pl


## Dozwolone etykiety

Etykietą (nazwą) w języku Python może być każdy ciąg "czarnych" znaków,
który:
 - nie jest [słowem kluczowym](
   https://docs.python.org/3/reference/lexical_analysis.html#keywords)
   (technicznie rzecz biorąc, słowa kluczowe to zarezerwowane nazwy),
 - rozpoczyna się literą alfabetu angielskiego lub znakiem podkreślenia
   ('\_'),
 - składa się z liter alfabetu angielskiego, cyfr i znaków podkreślenia.

```python
>>> None = 1
>>> def def(x):
...     pass
>>> 1e4 = 15
>>> e14 = 15
>>> print(e14)
```

W nazwach [wiellkie litery](https://pl.wikipedia.org/wiki/Majusku%C5%82a)
są odróżniane od [liter małych](
https://pl.wikipedia.org/wiki/Minusku%C5%82a).

```python
>>> A = 1
>>> a = 2
>>> print(A - a)
```

[Dokładne reguły opisujące poprawne nazwy w języku Python](
https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
są bardziej skomplikowane.  Przykładowo, w nazwach języka Python 3 (ale
nie Python 2) dozwolone są polskie znaki:

```python
>>> ą = 3
```

## Nazwy o specjalnym znaczeniu

 - `_nazwa` - delikatna sugestia, że jest to nazwa powiązana z obiektem
   o charakterze wewnętrznym, z którego korzysta się na własne ryzyko.

 - `__nazwa` - silna sugestia, że nazwa jest powiązana z obiektem
   o charakterze wewnętrznym.  Dostęp do takiego obiektu jest utrudniony
   (ale wciąż możliwy), gdyż "z zewnątrz" widnieje on pod bardziej
   skomplikowaną nazwa.  Nie zalecam stosowania.

 - `__nazwa__` - nazwa specjalna.  Nazwy te są zarezerwowane dla
   obiektów o ściśle okreslonym przeznaczeniu.  Nie należy samemu
   wymyślać nowych nazw specjalnych.


## Jak tworzyć dobre etykiety?

Jedną z etykiety jest poinformowanie czytelnika o intencji programisty.
Oznacza to, że nazwy powinny wskazywać na znaczenie obiektu, którego
dotyczą.  I tak `srednia_arytmetyczna` będzie lepszą nazwą niż `mi`
(lub `u`).  Jeszcze lepszą nazwą będzie `mean`.  Słowa kluczowe języka
Python pochodzą z języka angielskiego, zatem anglojęzyczne etykiety
ułatwią czytanie kodu.  Mówi sie, że dobrze napisany kod czyta się jak
dobrze napisaną prozę - odpowiedni dobór nazw jest tu kluczowy
(przypominam nazwy funkcji `even()` i `is_even()` z poprzednich zajęć).

Warto pamiętać, że nazwy są wymawialne podczas dyskusji na temat
programu.  W związku z tym nazwy trudne do wymówienia nie są dobre.

Czego unikać? Nazw mylących:

```python
>>> xxxxxxxxx = 1
>>> xxxxxxxx = 13
>>> print(xxxxxxxx < xxxxxxxxx)
>>> l1 = 11
>>> ll = 12
>>> print(l1 < 11)
>>> print(ll > 11)
>>> a0 = 0
>>> aO = 1
>>> print(a0 * ll - aO * 11)
```

Nazwy można zapisywać na różne sposoby.  Dla czytelności istotna jest
konsekwencja - najpierw na poziomie funkcji, później - pliku, projektu,
zespołu programistów, a wreszcie - całej społeczności.

[Wytyczne dla programistów języka Python](
https://www.python.org/dev/peps/pep-0008/#naming-conventions)
zawarte są w dokumencie PEP8, którego lekturę polecam.


## Zadanie 1

Zdefiniuj funkcję `state_of_water_at(temperature)` zwracającą
napis 'gas' gdy `temprerature > 100`, w przeciwnym
przypadku - napis `liquid`.


## Zadanie 2

Zmodyfikuj funkcję `state_of_water_at(temperature)` tak,
by zwracała napis 'solid' gdy `temprerature < 0`.


## "Instrukcja wyboru"

Teoretycznie nie występuje w języku Python, ale mamy odpowiadającą jej
"drabinkę `elif`-ów".

```python
def print_in_polish(n):
    if n == 0:
        print('zero')
    elif n == 1:
        print('jeden')
    elif n == 2:
        print('dwa')
    else:
        print('inny przypadek')
```

Odpowiada ona wielokrotnie zagnieżdżonym instrukcjom warunkowym:
```python
def print_in_polish(n):
    if n == 0:
        print('zero')
    else:
        if n == 1:
            print('jeden')
        else:
            if n == 2:
                print('dwa')
            else:
                print('inny przypadek')
```

Gdybyśmy zamiast drukowac, zwracali polskie słowa, moglibyśmy
funkcję znacznie uprościć:
```python
def in_polish(n):
    if n == 0:
        return 'zero'
    if n == 1:
        return 'jeden'
    if n == 2:
        return 'dwa'
    return 'inny przypadek'
```


Instrukcję warunkową czasem uznaje się za tzw. ["zapach kodu"](
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


## Zadanie 3

Usuń żagnieżdżenia instrukcji warunkowych z definicji funkcji
`state_of_water_at(temperature)`.


## Zadanie 4

Zdefiniuj funkcję `maximum(a, b)` zwracającą większą z liczb
`a` i `b`.


## Wyrażenie warunkowe

```python
a = 1
b = 2
minimum_of_a_and_b = a if a < b else b
```

Przy uzyciu instrukcji warunkowej trzeba byłoby napisać:

```python
if a < b:
    minimum_of_a_and_b = a
else:
    minimum_of_a_and_b = b
```


## Zadanie 5

Przepisz funkcję `maximum(a, b)` z użyciem wyrażenia warunkowego.


## Zadanie 6

Zdefiniuj funkcję `is_odd(n)` zwracającą `True` gdy `n` jest
nieparzyste, `False` w przeciwnym przypadku.


## Szablony tekstowe

```python
>>> template = 'Is {} > {}?'
>>> text = template.format(1, 2)
>>> print(text)
```

```python
>>> template = 'Is {0} > {1}? Or maybe {1} > {0}?'
>>> text = template.format(1, 2)
>>> print(text)
```

```python
>>> template = 'Is {a} > {b}? Or maybe {b} > {a}?'
>>> text = template.format(a=1, b=2)
>>> print(text)
```

[Więcej o szablonach tekstowych](
https://docs.python.org/3/library/stdtypes.html#str.format).


## Zadanie 7

Przepisz funkcję `is_odd(n)` tak, by wywołana drukowała dodatkowo
'is\_odd(<n>) called', gdzie '<n>' jest wartością `n`.


## Zadanie 8

Zastąp wywołanie funkcji `print()` wywołaniem funkcji
`logging.debug()`.  Co się zmieniło?


## Zadanie 9

Zmień poziom wrażliwości na `logging.DEBUG`.  Co się zmieniło?

[Więcej o rejestrowaniu zdarzeń](
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)


## Zadanie 10

Używając operatora logicznego `or` zdefiniuj funkcję `always(n)`
sprawdzajacą, czy liczba `n` jest parzysta lub nieparzysta.
Przetestuj funkcję na różnych liczbach. Co się dzieje?



## Zadanie 11

Używając operatora logicznego `and` zdefiniuj funkcję `never(n)`
sprawdzajacą, czy liczba `n` jest jednocześnie  parzysta lub nieparzysta.
Przetestuj funkcję na różnych liczbach. Co się dzieje?


## Leniwe operatory

```python
>>> print(is_even(1) and is_odd(1))
>>> print(is_even(2) and is_odd(2))
>>> print(0 and 123)
>>> print(1 and 123)
>>> print(is_even(1) or is_odd(1))
>>> print(is_even(2) or is_odd(2))
>>> print(1 or 123)
>>> print(0 or 123)
```


## Zadanie 12

Przepisz funkcje `always(n)` i `never(n)` używając wyrażeń
warunkowych zamiast operacji logicznych.  Co się dzieje?


## Zadanie 13

Zdefiniuj funkcję `pairity(n)` (ang. "parzystość") zwracającą `'even'`
dla parzystego `n` i `'odd'` dla nieparzystego.


## Zadanie 14

Dla liczb od 0 do 10 **włącznie** wypisz: liczbę i jej parzystość rozdzielone
znakiem tabulacji (`'\t'`).


## Jeszcze raz o iteracji

Dlaczego to nie działa?

```python
>>> numbers = [1, 2, 3]
>>> for x in numbers:
...     x = x + 1
>>> print(numbers)
>>> print(x)
```


## Pętla while

```python
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

## Po co nam petla for?

Kilka słów o zbiorach i słownikach.


## Jak ponumerować obiekty uzywając pętli for?

```python
numbers = [10, -20, 40]
for i, n in enumerate(numbers):
    print('{}\t{}'.format(i, n))
```


## Jesli zostanie czas

### Listy bardziej szczegółowo

### Sito Erastostenesa
