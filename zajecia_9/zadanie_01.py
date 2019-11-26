#!/usr/bin/python3

# Zastąp tę linię

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        make_enumerated_copy(sys.stdin, sys.stdout)

    elif len(sys.argv) == 2:
        with open(sys.argv[1]) as src:
            make_enumerated_copy(src, sys.stdout)

    elif len(sys.argv) == 3:
        with open(sys.argv[1]) as src:
            with open(sys.argv[2], 'w') as dst:
                make_enumerated_copy(src, dst)

    else:
        print('Usage: python3 {} [<src> [<dst>]]'.format(sys.argv[0]))

