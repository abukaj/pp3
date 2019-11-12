#!/usr/bin/python3

def append_one(numbers=[]):
    numbers.append(1)
    return numbers


if __name__ == '__main__':
    assert append_one([]) == [1]
    assert append_one([2]) == [2, 1]
    assert append_one() == [1], 'pierwsze wywolanie append_one()'
    assert append_one() == [1], 'drugie wywolanie append_one()'

