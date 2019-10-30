#!/usr/bin/python3

import logging


def is_odd(n):
    logging.debug('is_odd({}) called'.format(n))

    return n % 2 == 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    assert is_odd(1)
    assert not is_odd(0)
