Zajęcia 13
----------

## Kartkówka - rozwiązanie

```python
# -*- coding: utf-8 -*-
'''
123456
'''

def gaderypoluki(text,key='gaderypoluki'):
    # Preprocessing
    d={}
    for case_key in [key.upper(), key.lower()]:
        for a, b in zip(case_key[::2],case_key[1::2]):
            d[a]=b
            d[b]=a

    # Encoding
    encoded = ''
    for letter in text:
        encoded += d.get(letter, letter)
    return encoded
```

Czy coś tutaj wymaga poprawy? ;)


### Sygnatura funkcji jest ważna

Kilku osobom sprawdzaczka odrzuciła rozwiązanie bez testowania, gdyż
funkcja została zdefiniowana bez uwzględnienia podanej w zadaniu
sygnatury: `gaderypoluki(text, key='gaderypoluki')`.


### Wykorzystanie gotowych rozwiązań

Kilka rozwiązań było opartych na "[gotowcu](
https://github.com/imicadio/gaderypoluki)".  Jest to dopuszczalne,
jednak warto w takim wypadku:
- postarać się zrozumieć, jakie warunki muszą być spełnione, by
  "gotowiec" zadziałał,
- swoje zrozumienie przedstawić w postaci znaczących nazw.

Przepisanie "gotowców" bez ich zrozumienia może zaszkodzić bardziej,
niż dostarczenie niekompletnego, ale własnego rozwiązania - zwłaszcza,
gdy sprawdzający się zorientuje. ;-)


### Shabang

Tzw. "shabang" to "sha" ("#", inaczej "hasz") i "bang" ("!"). Formalnie
jest to komentarz (linia zaczyna się znakiem "#").

Jeśli program 'program.py' rozpoczyna się linią:
```python
#!/usr/bin/python3
```

wówczas wywołanie:
```bash
$ ./program.py opcjonalne argumenty
```
jest równoważne wywołaniu:
```bash
$ /usr/bin/python3 program.py opcjonalne argumenty
```
(zakładając, że posiadamy uprawnienia do wykonania pliku 'program.py').

Linia ta jest opcjonalna; raczej nie warto pisać: `#!usr/bin/python3`.


## Świąteczne dodatkowe zadanie domowe

Otrzymałem 8 śnieżynek, udzieliłem informacji zwrotnej autorom.  Jeśli
ktoś informacji nie dostał - proszę o kontakt, będziemy sprawę
wyjaśniać.


## Noworoczny Easter Egg

```python
import antigravity
```


## Pięciominutowa kartkówka

Stwórz moduł "kartkowka6.py".  Swój numer albumu wpisz w napisie
dokumentującym.

W module zdefiniuj funkcję `inverted(d)` zwracającą "odwrócony" słownik
`d`, tzn. że jeśli `d == {1:2, 33:4}`, to `inverted(d) == {2:1, 4:33}`.

Oczekuję 100% poprawności. ;)  (W porywach do 200%)


### Podpowiedzi

Déjà vu? ;)

Sprawdzaczka zawiera wysokopunktowany test specjalny.

### Przesłanie rozwiązania

Moduł "kartkowka6.py" zawierający rozwiązanie zadania należy przesłać
jako załącznik wiadomości e-mail zatytułowanej "Kartkówka 5" na dwa
adresy e-mail:
 - kartkowka20200108@amix.org.pl
 - j.m.dzik@nencki.edu.pl


## Pytania do zadania domowego?


## Zadania

**kontynuujemy zadania z poprzednich zajęć**

### Przypomnienie

[NumPy](https://brain.fuw.edu.pl/edu/index.php/PPy3/NumPy)
[Matplotlib](https://brain.fuw.edu.pl/edu/index.php/PPy3/Matplotlib)


### Zadanie 6

Wczytaj dane epidemiologiczne
(`np.loadtxt('diseases.csv', delimiter=',')`).

W pierwszej kolumnie jest rok, w drugiej - numer dwutygodniowego
(ok. 15 dni) okresu, w kolejnych - skumulowana (w okresach danego roku)
liczba zachorowań na (kolejno) grypę, ospę wietrzną i odrę.

Sprawdź poprawność danych (np. czy skumulowane liczby w każdym roku są
rosnące).


#### Preprocessing

Jeśli mamy czas - przetworzymy dane do postaci, w której każdemu okresowi
(z wyjątkiem pierwszego, który odrzucimy) odpowiadać będzie liczba
zarejestrowanych w nim zachorowań.  Jeśli czasu nie mamy - załadujemy
przetworzone dane (`np.load('diseases.npy')`).


#### Zadanie 6a

Dla każdej choroby przygotuj osobny wykres, a na nim dwie (opisane
w legendzie) krzywe przedstawiające liczbę zachorowań w odpowiednich
okresach - jedną dla roku 2018, drugą dla 2019.


#### Zadanie 6b

Wygładź krzywe za pomocą średniej ruchomej.  Poeksperymentuj z różną
długością okna i różnymi wagami.


#### Zadanie 6c

Dla każdej choroby przygotuj wykresy słupkowe pokazujące liczbę
zachorowań w kolejnych miesiącach od października 2017 (włącznie)
do listopada 2019 (włącznie).



### Zadanie 7 - metoda Eulera

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


### Zadanie 8 - porównanie zbieżności metody bisekcji z metodą Newtona

#### Zadanie 8a

Na poprzednich zajęciach implementowali Państwo metodę bisekcji
(zad. 2a) dla funkcji `f(x) = x ** 2 - 2`.  Proszę zmodyfikować
implementację tak, żeby zapamietywała (np. dopisując do listy) wartości
punktu środkowego dla kolejnych kroków metody.


#### Zadanie 8b

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


#### Zadanie 8c

Wartość miejsca zerowego funkcji jest znana (`np.sqrt(2)`).  Proszę
wykreślić na jednym wykresie krzywe pokazujące wartość bezwzględną błędu
metod w kolejnych krokach.  Proszę spróbować użyć skali logarytmicznej
dla osi rzędnych.


