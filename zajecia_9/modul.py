#!/usr/bin/python3
import sys

print('wykonuję plik "{}"'.format(__file__),
      end=' ',
      file=sys.stderr)

#################### POCZATEK DEFINICJI ###############################

def factorial(n):
    print('called {}.factorial({})'.format(__name__,
                                           n))
    if n == 0:
        return 1
    return n * factorial(n - 1)

def make_enumerated_copy(src, dst):
    for i, line in enumerate(src):
        dst.write('{:03d}\t{}'.format(i, line))

#################### KONIEC DEFINICJI #################################

if __name__ == '__main__':
    print('jako program',
          file=sys.stderr)

else:
    print('jako moduł',
          file=sys.stderr)
