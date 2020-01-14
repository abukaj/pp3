Zajęcia 13
----------

## Kartkówka - rozwiązania

```python
'''
123456
'''
def inverted(d):
    result = {}
    for k in d:
        result[d[k]] = k

    return result
```

lub:

```python
'''
123456
'''
def inverted(d):
    return {d[k]: k for k in d}
```


### Sprawdzenie typu

```python
>>> slownik = {}
>>> print(isinstance(slownik, dict))
>>> lista = []
>>> print(isinstance(lista, dict))
```


### Appendujemy tylko do listy

Metoda `.append()` ma sens tylko w przypadku obiektów typu `list`.

```python
>>> lista = []
>>> lista.append(1)
>>> print(lista)
[1]
>>> lista.append(2)
>>> print(lista)
[1, 2]
```

```python
>>> liczba = 1
>>> liczba.append(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'append'
```

```python
>>> slownik = {}
>>> slownik[1] = 2
>>> slownik[1].append(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'append'
```


## Na rozgrzewkę

Narysuj [lemniskatę Gerona](
https://pl.wikipedia.org/wiki/Lemniskata_Gerona):

```python
X = (T ** 2 - 1) / (T**2 + 1)
Y = 2 * T * (T**2 - 1)  / (T**2 + 1)**2
```

dla `-t_max <= T <= t_max` i różnych wartości `t_max`.



## Kartkówka

Stwórz moduł "kartkowka7.py".  Swój numer albumu wpisz w napisie
dokumentującym.

W module zdefiniuj funkcję `median(iterable)` zwracającą
[wartość środkową](https://pl.wikipedia.org/wiki/Mediana) (medianę)
elementów iteratki `iterable`.  Przyjmij, że wartość środkowa dla pustej
iteratki wynosi `None`. 


### Podpowiedzi

Iteratka może nie być sekwencją, ani nawet nie posiadać metody
`.__len__()` (przez co na iteratce nie można będzie wywołać funkcji
`len()`).

```python
>>> help(sorted)
```


### Przesłanie rozwiązania

Moduł "kartkowka7.py" zawierający rozwiązanie zadania należy przesłać
jako załącznik wiadomości e-mail zatytułowanej "Kartkówka 7" na dwa
adresy e-mail:
 - kartkowka20200115@amix.org.pl
 - j.m.dzik@nencki.edu.pl


## Zadania

### Przypomnienie

[NumPy](https://brain.fuw.edu.pl/edu/index.php/PPy3/NumPy)
[Matplotlib](https://brain.fuw.edu.pl/edu/index.php/PPy3/Matplotlib)


### Zadanie 1

Napisz program wizualizujący [obliczanie pi metodą Monte Carlo](
https://www.smbc-comics.com/comic/math-and-war):

1. Wylosuj dużo (ale nie za dużo, powiedzmy `n = 100`) par liczb
   rzeczywistych z rozkładu jednorodnego na przedziale od `-1` do `1`.
   Pary te wypełnią wnętrze kwadratu o boku `2`.
2. Policz ile (`m`) par zostało wylosowanych w kole o środku w poczatku
   układu współrzędnych i jednostkowym promieniu.
3. Pole kwadratu to `4`, zaś koła - `pi`.  Stąd można oczekiwać, że
   prawdopodobieństwo wylosowania pary należącej do koła to `pi / 4`.
   Prawdopodobieństwo to można przybliżyć jako `m / n`, zatem mamy
   `pi ~ 4 * m / n`.

Wykreśl kwadrat i koło **(powinny tworzyć trochę inny wzór niż
na tarczy żołnierza)**.  Zaznacz wylosowane pary.  Jako tytuł obrazka
ustaw obliczone przybliżenie `pi`.  Zapisz obrazek.


#### Podpowiedź

```python
ax = plt.gca()
ax.set_aspect('equal')
```


### Zadanie 1a

Uruchom program jeszcze raz.  Czy układ par bądź przybliżona wartość
są takie same?

Zmodyfikuj program tak, by jego kolejne uruchomienia były powtarzalne.


### Zadanie 1b

Dla różnych wartości `n` tworzących ciag geometryczny (przynajmniej
`[10, 100, 1000, 10000]`) oblicz kilkakrotnie (co najmniej `k = 10 `
razy) przybliżenie liczby pi.

Zwizualizuj na dwa sposoby zmiany dokładności przybliżenia w zależności
od wartości `n`: raz jako przybliżone wartości, a raz jako wartości
bezwzględne błędu przybliżenia.  Wykresy powinny dzielić oś odciętych.

#### Podpowiedź

[Wykres punktowy](https://pl.wikipedia.org/wiki/Wykres_punktowy)
(ang. "scatter plot").

[Shared axis demo](
https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/shared_axis_demo.html)



### Zadanie 2

Jeśli ciało w chwili `t = 0` znajdowało się na wysokości `y = 0`
i zostało pionowo rzucone z predkością `v0`, wówczas jego chwilowa
wysokość dana jest funkcją `y(t) = v0 * t + g * t **2 / 2`.

Ruch ten mozna również zasymulowac stosując [metodę Eulera](
https://pl.wikipedia.org/wiki/Metoda_Eulera):

```python
y(t + h) = y(t) + v(t) * h
v(t + h) = v(t) + g * h
```

(`h` to tzw. *krok symulacji*)


Proszę przeprowadzić symulację dla różnych wartości `h` i przygotować
dwa wykresy (w jednym oknie).  Na pierwszym proszę wykreślić dokładny
wykres `y(t)` oraz wyniki symulacji.  Na drugim proszę wykreślić
zależność błędu od `t` (dla każdej wartości `h` osobną krzywą; krzywe
dla początku symulacji nie musza byc widoczne w całości).


**kontynuujemy zadania z poprzednich zajęć**


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



### Zadanie 7 - symulacja Księżyca

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


