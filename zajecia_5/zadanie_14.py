#!/usr/bin/python3

def pairity(n):
    return 'odd' if n % 2 else 'even'


if __name__ == '__main__':
    assert pairity(1) == 'odd'
    assert not pairity(0) == 'even'

    # Tu umieść rozwiązanie
