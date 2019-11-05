#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    result = 0.

    for value in sys.argv[1:]:
        result += float(value)

    print(result)

