Ćwiczenia informacyjne i komunikacyjne (pracownia 2019)
-------------------------------------------------------


## Jak pobrać materiały ćwiczeniowe

W ramach eksperymentu spróbujemy użyć profesjonalnego narzędzia
programistycznego ([Git](https://git-scm.com/)) do pobierania
przygotowanych przeze mnie materiałów ćwiczeniowych.  Jeśli się nam
uda, będę mógł przygotowaywać dla Państwa wstępnie napisane programy
wymagające uzupełnienia bądź poprawienia.  Jeśli się nie uda, będziemy
pracować w dotychczasowym trybie.

### Jak skonfigurować Git-a?

Proszę ustawić katalog z zajęciami jako roboczy.  Jeśli stosowali się
Państwo do moich sugestii, powinna to załatwić komenda podobna do:

```bash
$ cd ~/cwiczenia/technologie_informacyjne_i_komunikacyjne
```

Przypominam o istotnych zaletach automatycznego uzupełniania (klawisz
tabulacji). ;)

Kolejne komendy "powiążą" katalog roboczy z repozytorium na platformie
[GitHub](https://github.com/) w którym znajduje się czytany właśnie
przez Państwa dokument:

```bash
$ git init
$ git remote add origin https://github.com/abukaj/pp3.git
$ git fetch
$ git checkout master
```

Komenda `git` jest przydatnym narzędziem do [kontroli wersji](
https://pl.wikipedia.org/wiki/System_kontroli_wersji).  Niestety nauka
kontroli wersji wykracza poza program naszych zajęć -- pozostawiam to
chętnym w ramach samodzielnego rozwoju.  Na zajęciach planuję używać
wyłącznie polecenia `git pull`, pobierającego najnowszą wersję
materiałów z repozytorium.
