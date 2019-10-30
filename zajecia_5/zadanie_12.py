#!/usr/bin/python3

import logging


def is_odd(n):
    logging.debug('is_odd({}) called'.format(n))

    return n % 2 == 1


def is_even(n):
    logging.debug('is_even({}) called'.format(n))

    return n % 2 == 0


def always(n):
    return is_even(n) or is_odd(n)


def never(n):
    return is_even(n) and is_odd(n)


if __name__ == '__main__':
    assert is_odd(1)
    assert not is_odd(0)
    assert is_even(2)
    assert not is_even(2)

    logging.basicConfig(level=logging.DEBUG)
    always(1)
    always(22)
    never(333)
    never(4444)
