Zajęcia 10
----------

## Zadanie na rozgrzewkę

Zdefiniuj funkcję `count(items)` zwracającą słownik, którego
kluczami bedą elementy "iteratki" (ang. "iterable") `items`,
a wartościami - liczba wystąpień elementu w "iteratce".
Załóż, że wszystkie elementy iteratki sa haszowalne.

### Try,except,else,finally


## Kartkówka

Tym razem bez szablonu.

Stwórz moduł "kartkowka3.py".  W komentarzu w drugiej linii modułu
wpisz swój numer albumu.  Zadanie zostanie opisane podczas zajęć.


### Przesłanie rozwiązania

Moduł "kartkowka3.py" zawierający rozwiązanie zadania należy przesłać
jako załącznik wiadomości e-mail zatytułowanej "Kartkówka 3" na dwa
adresy e-mail:
 - kartkowka20191204@amix.org.pl
 - j.m.dzik@nencki.edu.pl

**Proszę sprawdzić pred wysłaniem, czy próba uruchomienia programu
nie kończy się błędem składni**


## Zadania na kolekcje

**podane w trakcie**

**bisekcja?**


## NumPy

**Zadanie 4 z poprzedniej listy**

### Ciekawostka
```python
import numpy as np
eps = np.finfo(float).eps
print(eps)
print(1 + eps - 1)
print(eps / 2)
print(1 + eps / 2 - 1)
print(np.arange(1 - eps, 1 + eps, eps/10))
print(np.arange(1 - eps, 1 + eps, eps/10) - 1)
print(np.linspace(1 - eps, 1 + eps, 20) - 1)
print(np.arange(0, 10, 0.5))
print(np.linspace(0, 10, 20))
print(np.linspace(0, 10, 20, endpoint=False))
```

`arange` a `linspoace`

### Ciekawostka 2

```python
A = np.array([1, 2, 3])
print(A * 0.5)
A *= 0.5  # Sam nie wiem, co to zrobi w tej wersji ;)
print(A)
```


### Zadania
[NumPy](https://brain.fuw.edu.pl/edu/index.php/PPy3/NumPy)


## Na kolejne zajęcia

[Matplotlib](https://brain.fuw.edu.pl/edu/index.php/PPy3/Matplotlib)
