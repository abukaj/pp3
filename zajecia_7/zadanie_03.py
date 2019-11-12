#!/usr/bin/python3

def multiply(A, B):
    return [a * B[i] for i, a in enumerate(A)]

if __name__ == '__main__':
    assert multiply([], []) == []
    assert multiply([1], [2]) == [2]
    assert multiply([1, 2], [3, 4]) == [3, 8]

