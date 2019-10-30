#!/usr/bin/python3

def maximum(a, b):
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    assert maximum(0, 0) == 0
    assert maximum(1, 0) == 1
    assert maximum(1, 2) == 2
