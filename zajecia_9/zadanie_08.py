#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    is_prime_candidate = [False, False] + [True] * (n - 1)
    last_tested = 1
    primes = set()

    for tested in range(n + 1):
        # TODO: kontynuuj jesli last_tested nie jest kandydatem
        #       na liczbe pierwsza
        # TODO: w przeciwnym razie dodaj tested do zbioru primes
        # TODO: przypisz wartośc False wszystkim elementom
        #       is_prime_candidate o indeksie wiekszym od tested bedacym
        #       wielokrotnoscia tested
        #
        #       NIEZMIENNIKI PETLI:
        #       * is_prime_candidate[i] dla i > tested zawiera True
        #         wtedy i tylko wtedy, gdy i nie jest wielokrotnoscia
        #         zadnej liczby ze zbioru primes
        #       * is_prime_candidate[i] dla i <= tested zawiera True
        #         wtedy i tylko wtedy, gdy i jest liczba pierwsza

        assert primes == {i for i, is_prime in enumerate(is_prime_candidate[:tested+1])
                          if is_prime}
    return primes


if __name__ == '__main__':
    # assert sieve_of_eratosthenes(1) == set()
    # assert sieve_of_eratosthenes(2) == {2}
    # assert sieve_of_eratosthenes(3) == {2, 3}
    # assert sieve_of_eratosthenes(4) == {2, 3}
    # assert sieve_of_eratosthenes(5) == {2, 3, 5}

