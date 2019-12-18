#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
123456

To jest napis dokumentujący modułu.
'''

def rot13(text):
    """
    Funkcja szyfrująca rot13

    To jest napis dokumentujący funkcji.
    """
    encoded = ''
    for letter in text:
        if letter < 'N':
            encoded += chr(ord(letter) + 13)

        else:
            encoded += chr(ord(letter) - 13)

    return encoded
