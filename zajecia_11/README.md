Zajęcia 11
----------

## Kartkówka

Tym razem bez szablonu.

Stwórz moduł "kartkowka4.py".  Swój numer albumu wpisz w [napisie
dokumentującym](https://pl.python.org/docs/tut/node6.html#l2h-8) (ang.
"docstring") modułu: umieszczonej na samym początku modułu stałej
tekstowej bez przypisanej etykiety.

Zadanie zostanie opisane podczas zajęć.

### Podpowiedzi

```python
ord('A')
ord('Z')
chr(ord('A') + 13)
chr(ord('N') + 13)
chr(ord('Z') + 13)
```


### Przesłanie rozwiązania

Moduł "kartkowka4.py" zawierający rozwiązanie zadania należy przesłać
jako załącznik wiadomości e-mail zatytułowanej "Kartkówka 4" na dwa
adresy e-mail:
 - kartkowka20191211@amix.org.pl
 - j.m.dzik@nencki.edu.pl


## Zadania

**omówić i dalej próbujemy robic samodzielnie**

### Przypomnienie

[NumPy](https://brain.fuw.edu.pl/edu/index.php/PPy3/NumPy)
[Matplotlib](https://brain.fuw.edu.pl/edu/index.php/PPy3/Matplotlib)

```python
import matplotlib.pyplot as plt
plt.plot(X, Y)
plt.show()
```

### Zadanie 1

Narysuj wykres funkcji `f(x) = x / pi * exp(-x / pi)` na przedziale
od 0 do 2 pi.


### Zadanie 1a - całkowanie numeryczne

Oblicz [metodą trapezów](
https://pl.wikipedia.org/wiki/Ca%C5%82kowanie_numeryczne#Metoda_trapez%C3%B3w)
całkę oznaczoną (na przedziale od 0 do 2 pi) funkcji z poprzedniego zadania.

Jak zmienia się wynik w zależności od liczby podprzedziałów?


### Zadanie 2

Narysuj wykres funkcji `f(x) = x ** 2 - 2` na przedziale od -2 do 2

W jakich miejscach przypada miejsce zerowe funkcji?


### Zadanie 2a - metoda bisekcji

Używając [metody bisekcji](
https://pl.wikipedia.org/wiki/Metoda_r%C3%B3wnego_podzia%C5%82u) znajdź
wartość dodatniego miejsca zerowego funkcji z poprzedniego zadania
z dokładnością `np.finfo(float).eps`.


## Dalsze zagadnienia do pracy własnej

[Tematy dodatkowe](https://brain.fuw.edu.pl/edu/index.php/PPy3/TematyDodatkowe)

[Zasady ,,Dobrej praktyki"](https://brain.fuw.edu.pl/edu/index.php/PPy3/DobrePraktyki)
