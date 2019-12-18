Zajęcia 12
----------

## Kartkówka - rozwiązanie

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
123456

To jest napis dokumentujący modułu.
'''

def rot13(text):
    """
    Funkcja szyfrująca rot13

    To jest napis dokumentujący funkcji.
    """
    encoded = ''
    for letter in text:
        if letter < 'N':
            encoded += chr(ord(letter) + 13)

        else:
            encoded += chr(ord(letter) - 13)

    return encoded
```

### Napisy dokumentujące

Do napisu dokumentującego można się dostać z poziomu języka Python:

```python
>>> import kartkowka4
>>> print(kartkowka4.__doc__)

123456

To jest napis dokumentujący modułu.

>>> help(kartkowka4)
>>> print(kartkowka4.rot13.__doc__)

    Funkcja szyfrująca rot13

    To jest napis dokumentujący funkcji.

>>> help(kartkowka4.rot13)
```

Komentarze są z definicji całkowicie ignorowane przez język Python,
więc są z jego poziomu nieosiągalne.

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# To jest zwykły komentarz
# a nie żaden napis
```

### Iteracja w sposób "Pythonowy"

Co jest czytelniejsze:

```python
for i in range(len(text)):
    letter = text[i]
    ...
```

czy:

```python
for letter in text:
    ...
```

???

## Zasady dobrej praktyki

[Zasady ,,Dobrej praktyki"](https://brain.fuw.edu.pl/edu/index.php/PPy3/DobrePraktyki)

W skrócie: Piszcie programy czytelne dla ludzi, komputery sobie poradzą.
W drugą stronę to rzadko działa.

### Herezja

Podstawową wartością oprogramowania (ang. "software") jest jego
"miękkość" (ang. "soft") - plastyczność, czyli łatwość wprowadzania
zmian.
Paradoksalnie, poprawność działania jest wartością drugorzędną.
Niepoprawny lecz "miękki" niepoprawny program można szybko poprawić.
Wprowadzenie nawet drobnej zmiany w "twardym" programie to droga
przez mękę.

### Jakość kodu i komentarze:

Jednostka jakości kodu to `WTF / min` - im mniej, tym lepiej.

Unikajcie komentarzy.  Komentarz jest potrzebny by wyjaśniać
zaskakujące fragmenty kodu (patrz wyżej).  Najlepszy komentarz to
taki, którego nie trzeba pisać.  Niektórzy sugerują, by zaczynać
komentarze słowami: *"przepraszam, że napisałem kod tak nieczytelnie,
że muszę go objaśniać komentarzem"*.  Tak więc gdy chcecie napisać
komentarz, zastanówcie się, czy możecie zmienić swój kod tak, by
komentarz stał się zbędny.

Przykład:
```python
if k < 77:  # 77 is ASCII code for 'N'
   ...
```

```python
if k < ord('N'):
    ...
```

```python
if letter < 'N':
   ...
```

```python
ascii_code_of_N = ord('N')

...


if ascii_code < ascii_code_of_N:
   ...
```

```python
def is_less_than_ascii_code_of_N(x):
    return x < ascii_code_of_N

...

if is_less_than_ascii_code_of_N(ascii_code):
    ...
```


### Bożonarodzeniowy Easter Egg

```python
import this
```


## Lambda - wyrażenia

Lambda wyrażenia to wyrażenia (nie definicje), które dają anonimową
(czyli nie nazwaną) funkcję.

```python
def f(x):
    return x**2

print(f(2))
print(f.__name__)


g = lambda x: x**2  # TAK SIĘ NIE ROBI!!!  Jesli funkcja ma mieć nazwę,
print(g.__name__)   # należy ją normalnie zdefiniować.
print(g(2))


for y in map(lambda x: x**2, range(10)):  # Tak się robi:-). Do tego
    print(y)                              # właśnie są lambda-wyrażenia.
```


## Kartkówka harcerska ;-)

Ponownie bez szablonu.

Stwórz moduł "kartkowka5.py".  Swój numer albumu wpisz w napisie
dokumentującym.

W module zdefiniuj funkcję `gaderypoluki(text, key='gaderypoluki')`
implementującą klasyczny harcerski szyfr [Gadery Poluki](
http://klobuck.zhp.pl/o-nas-2/do-pobrania/materialy-dla-harcerzy/szyfry/#gadery).

Funkcja powinna przyjmować dwa parametryy tekstowe: tekst jawny
i (opcjonalnie) klucz będący parzystej długości napisem złożonym
z niepowtarzających się liter (wielkie i małe powinny być
traktowane równoważnie).  Domyślna wartość tego parametru to oczywiście
'gaderypoluki', ale są też inne szyfry harcerskie z tej rodziny, które
powinna implementować funkcja:
- Koniec matury (`key='KoniecMatury'`),
- Malinowe buty (`key='MalinoweButy'`),
- Nowe buty lisa (`key='NoweButyLisa'`),
- KC-minutowy (`key='KaCeMinutowy'`),
- Polityka Renu (`key='PolitykaRenu'`),
- Gubi kalesony (`key='GubiKalesony'`),
- Kalinowe buty (`key='KalinoweButy'`),
- Halo jupitery (`key='HaloJupitery'`),
- Parę kilo gumy (`key='PareKiloGumy'` - bez polskich znaków),
- Koniec matury (`key='KoniecMatury'`),
- Bitwa o chmury (`key='BitwaOChmury'`),
- Motyle cudaki (`key='MotyleCudaki'`),
- Regulaminowy (`key='regulaminowy'),
- To my, badeluki (`key='ToMyBadeluki'`),
- itp.

Tym razem nie bedę "ręcznie" uznawać testów nie uznanych przez
sprawdzaczkę, dlatego **proszę upewnić się**, że:
- moduł importuje się bez błędów,
- moduł posiada napis dokumentujący z 6-cyfrowym numerem Państwa albumu,
- funkcja zwraca obiekt właściwego typu (`str`).


### Podpowiedzi
```python
d = {'a': 'g'}
for letter in 'ayb':
    try:
        print(d[letter])
    except KeyError:
        print(letter)

    print(d[letter] if letter in d else letter)

    print(d.get(letter, letter))

string = 'aged'
for case_string in [string.upper(),
                    string.lower()]:
    for a, b in zip(case_string[::2],
                    case_string[1::2]):
        print(a, b)
        print(b, a)
```


### Przesłanie rozwiązania

Moduł "kartkowka5.py" zawierający rozwiązanie zadania należy przesłać
jako załącznik wiadomości e-mail zatytułowanej "Kartkówka 5" na dwa
adresy e-mail:
 - kartkowka20191218@amix.org.pl
 - j.m.dzik@nencki.edu.pl


## Zadania

**omówić i dalej próbujemy robic samodzielnie**

### Przypomnienie

[NumPy](https://brain.fuw.edu.pl/edu/index.php/PPy3/NumPy)
[Matplotlib](https://brain.fuw.edu.pl/edu/index.php/PPy3/Matplotlib)


### Zadanie 1

Zdefiniować funkcję `christmas_tree(n)` rysującą na ekranie choinkę
o `n` poziomach:

```
     *
    ***
   *****
  *******
    ***
   *****
  *******
 *********
   *****
  *******
 *********
***********
    ###
```

(tu choinka ma 3 poziomy)

Można użyć innych znaków:
```
     A
    AAA
     A
    AAA
   AAAAA
    AAA
   AAAAA
  AAAAAAA
    HHH
```

a nawet dodać losowo pojawające się bombki (`import random`) i inne
ozdoby:

```
    \|/
   --X--
    /A\
    AAA
   AAAAA
  AAAAAAA
    AAA
   AAAAA
  AAAAAAA
 AAAAAAAAA
   AAAAA
  AAAAAAA
 AAAAAAAAA
AAAAAAAAAAA
    HHH

```

### Zadanie 2

Narysuj choinkę używając pakietu [Matplotlib](
https://brain.fuw.edu.pl/edu/index.php/PPy3/Matplotlib).


### Zadanie 3

Wyświetl (w jednym oknie) trzy histogramy.  Pierwszy powinien
przedstawiać rozkład długości linii w pliku `reduta.txt`, drugi -
rozkład długości słów, trzeci - rozkład liczby słów w linii.  Jeśli to
możliwe, dobierz liczby przedziałów klasowych (parametr `bins=`) tak,
by histogramy dawały przejrzysty obraz rozkładów.

#### Podpowiedź

```python
plt.subplot(1, 3, 2)
```

### Zadanie 4

Wyświetl wykres funkcji `y = np.pi * x ** np.e`
dla x od `1e-5` do `1e5`.

Wyświetl wykres jeszcze raz - tym razem użyj skali logarytmicznej dla
obydwu osi.  Jeśli to potrzebne, użyj `np.logspace(-5, 5, ...)` do
uzyskania na osi odciętych wartości będących kolejnymi wyrazami ciągu
geometrycznego.


### Zadanie 5

Wyświetl histogram rozkładu log-normalnego:

```python
DATA = np.random.lognormal(size=1000)
```

Rozkład ten ma ciężki prawostronny ogon.  Pomimo tego można go
przedstawić w sposób czytelny (nie używając przekształceń typu
`np.log()`).

#### Podpowiedź

Użyj logarytmicznej skali dla osi odciętych oraz granic przedziałów
klasowych będących kolejnymi wyrazami ciągu geometrycznego
(`bins=np.logspace(...)`).


### Zadanie 6 - metoda Eulera

Księżyc (którego masa nie jest istotna) w chwili 0 znajduje się
w apogeum (`position = np.array([405.696e9, 0])` m), zaś Ziemia
(o masie `mass_of_earth = 5.97219e24` kg) - w punkcie początkowym układu
współrzędnych.  Prędkość księżyca `velocity = np.array([0, 968e6])`.
Jeśli zaniedbamy grawitację Słońca i to, że tak Księżyc jak i Ziemia
okrążają wspólne [barycentrum](
https://pl.wikipedia.org/wiki/%C5%9Arodek_ci%C4%99%C5%BCko%C5%9Bci),
możemy uznać, że Księżyc porusza się z przyspieszeniem
`acceleration = -gravity_constant * mass_of_earth * position / (position**2).sum() ** 1.5`
(`gravity_constant = 6.67408e-11`).

Stosując [metodę Eulera](https://pl.wikipedia.org/wiki/Metoda_Eulera)
możemy zasymulować ruch Księżyca po orbicie:

```python
position += velocity * h
velocity += acceleration * h
```

(`h` to tzw. *krok*)

Proszę narysować na jednym wykresie tor ruchu księżyca w ciągu ok.
3 miesięcy dla różnych wartości kroku.  **Uwaga: jednostką kroku
jest sekunda**, proszę więc zaczynać od **możliwie dużych** kroków
i oszacować **przed rozpoczęciem obliczeń i rysowania**, ile kroków
przypadnie na 3 miesiące.


### Zadanie 7 - porównanie zbieżności metody bisekcji z metodą Newtona

#### Zadanie 7a

Na poprzednich zajęciach implementowali Państwo metodę bisekcji
(zad. 2a) dla funkcji `f(x) = x ** 2 - 2`.  Proszę zmodyfikować
implementację tak, żeby zapamietywała (np. dopisując do listy) wartości
punktu środkowego dla kolejnych kroków metody.


#### Zadanie 7b

Krok [metoda Newtona](https://pl.wikipedia.org/wiki/Metoda_Newtona)
dla naszej funkcji będzie mieć postać:

```python
x -= (x ** 2 - 2.0) / (2 * x)
```

Proszę (**zaczynając od `x > 0`**) zaimplementować metodę Newtona tak,
by:
- zapamietywała kolejne przybliżenia miejsca zerowego (`x`),
- zakończyła pracę, gdy wartość bezwzględna różnicy dwóch ostatnich
  przybliżeń wyniesie mniej niż `2 * np.finfo(float).eps`.




## Dalsze zagadnienia do pracy własnej

[Tematy dodatkowe](https://brain.fuw.edu.pl/edu/index.php/PPy3/TematyDodatkowe)

[Zasady ,,Dobrej praktyki"](https://brain.fuw.edu.pl/edu/index.php/PPy3/DobrePraktyki)
