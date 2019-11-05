#!/usr/bin/python3

def index_of_first_greater_harmonic_number(x):
    harmonic_number = 0.0

    for i in range(1000):
        harmonic_number += 1.0 / i
        if harmonic_number > x:
            return i


if __name__ == '__main__':
    assert index_of_first_greater_harmonic_number(0) == 1
    assert index_of_first_greater_harmonic_number(1) == 2
    assert index_of_first_greater_harmonic_number(1.49) == 2
    assert index_of_first_greater_harmonic_number(1.5) == 3
    # assert index_of_first_greater_harmonic_number(8) == 1674
