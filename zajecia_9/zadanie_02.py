#!/usr/bin/python3

def copy_text_in_uppercase(src, dst):
    pass


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        copy_text_in_uppercase(sys.stdin, sys.stdout)

    elif len(sys.argv) == 2:
        with open(sys.argv[1]) as src:
            copy_text_in_uppercase(src, sys.stdout)

    elif len(sys.argv) == 3:
        with open(sys.argv[1]) as src:
            with open(sys.argv[2], 'w') as dst:
                copy_text_in_uppercase(src, dst)

    else:
        print('Usage: python3 {} [<src> [<dst>]]'.format(sys.argv[0]))

