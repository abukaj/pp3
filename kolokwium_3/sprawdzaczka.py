#!/usr/bin/python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    import re
    import sys
    if sys.version_info.major < 3:
        ModuleNotFoundError = ImportError
    
    try:
        import vigenere
    except (ModuleNotFoundError, ImportError):
        print("Zdefiniuj moduł vigenere.py")
        exit()
    except Exception as e:
        print("Błąd w module vigenere.py uniemożliwiający jego import:")
        print(repr(e))
        exit()
    
    score_decode = 0
    score_encode = 0
    debug_decode = []
    debug_encode = []
    for plaintext, key, ciphertext in [
        ('', '', ''),
        ('pies', 'AAAA', 'PIES'),
        ('to', 'AAA', 'TO'),
        ('pies', 'A', 'PIES'),
        ('tojes', 'TAJNE', 'MOSRW'),
        ('tojestbardzo', 'TAJNE', 'MOSRWMBJEHSO'),
        ('to jest bardzo tajny tekst', 'TAJNE', 'MO SRWM BJEHSO CNNGY CROLT')
        ]:
        try:
            res = vigenere.szyfruj(key, plaintext)
        except Exception as e:
            debug_encode.append('({!r}, {!r})\nfailed with\n{!r}'.format(
                                    key, plaintext, e))
        else:
            if res == ciphertext:
                score_encode += 1
            else:
                debug_encode.append('({!r}, {!r})\nbad output\n{!r}\n{!r}'.format(
                                         key, plaintext, ciphertext, res))

        try:
            res = vigenere.odszyfruj(key, ciphertext)
        except Exception as e:
            debug_decode.append('({!r}, {!r})\nfailed with\n{!r}'.format(
                                     key, ciphertext, e))
        else:
            if res == plaintext.upper():
                score_decode += 1
            else:
                debug_decode.append('({!r}, {!r})\nbad output\n{!r}\n{!r}'.format(
                                         key, ciphertext, plaintext.upper(), res))
    
    print('vigenere.szyfruj(): {}'.format(score_encode))
    print('vigenere.odszyfruj(): {}'.format(score_decode))
    print()
    print('DEBUG')
    for msg in debug_encode:
        print('vigenere.szyfruj' + msg)
    for msg in debug_decode:
        print('vigenere.odszyfruj' + msg)

    print()
    print('vigenere.szyfruj(): {}'.format(score_encode))
    print('vigenere.odszyfruj(): {}'.format(score_decode))
