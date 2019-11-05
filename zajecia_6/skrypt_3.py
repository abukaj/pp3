#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print('Usage: {} <number a> <number b>'.format(sys.argv[0]))

    else:
        print(float(sys.argv[1]) - float(sys.argv[2]))

