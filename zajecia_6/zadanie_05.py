#!/usr/bin/python3

def increased(items):
    result = []

    for n in items:
        result.append(n + 1)

    return result


if __name__ == '__main__':
    assert increased([]) == []
    assert increased([0]) == [1]
    assert increased([-1, 2]) == [0, 3]

