#!/usr/bin/python3

from zadanie_02 import make_enumerated_copy
# from rozwiazanie_02 import make_enumerated_copy

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} <src> <dst>'.format(sys.argv[0]))

    else:
        with open(sys.argv[2], 'w') as dst:
            with open(sys.argv[1]) as src:
                make_enumerated_copy(src, dst)

