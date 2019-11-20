#!/usr/bin/python3

def make_enumerated_copy(src, dst):
    for i, line in enumerate(src):
        dst.write('{:03d}\t{}'.format(i, line))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} <src> <dst>'.format(sys.argv[0]))

    else:
        with open(sys.argv[2], 'w') as dst:
            with open(sys.argv[1]) as src:
                make_enumerated_copy(src, dst)

