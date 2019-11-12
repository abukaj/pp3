#!/usr/bin/python3

def primes_up_to(n):
    candidates = # TODO: sekwencja liczb od 2 do n
    primes = # TODO: zbior pusty

    # NIEZMIENNIKI PETLI
    # ------------------
    #

    while candidates:
        next_prime = # TODO: kolejna liczbe pierwsza
        # TODO: dodaj liczbe next_prime do zbioru primes
        # TODO: zastap sekwencje candidates nowa tak, by zachowac
        #       NIEZMIENNIKI PETLI:
        #       * sekwencja candidates zawiera wszystkie liczby
        #         naturalne od 2 do n niepodzielne przez liczby
        #         w zbiorze primes,
        #       * sekwencja candidates jest uporządkowana

    return primes


if __name__ == '__main__':
    # assert primes_up_to(1) == set()
    # assert primes_up_to(2) == {2}
    # assert primes_up_to(3) == {2, 3}
    # assert primes_up_to(4) == {2, 3}
    # assert primes_up_to(5) == {2, 3, 5}

