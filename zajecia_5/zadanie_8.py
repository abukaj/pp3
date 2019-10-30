#!/usr/bin/python3

import logging


def is_odd(n):
    return n % 2 == 1


if __name__ == '__main__':
    assert is_odd(1)
    assert not is_odd(0)
