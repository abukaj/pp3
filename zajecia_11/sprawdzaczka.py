#!/usr/bin/python3

import codecs
encode = codecs.encode
def doNotCheat(*args, **kwargs):
    raise RuntimeError("Nie korzystaj z codecs.encode()")

codecs.encode = doNotCheat

try:
    import kartkowka4
except (ModuleNotFoundError, ImportError):
    print("Zdefiniuj moduł kartkowka4.py")
    exit()
except Exception as e:
    print("Błąd w module kartkowka4.py uniemożliwiający jego import:")
    print(repr(e))
    exit()

if not hasattr(kartkowka4, 'rot13'):
    print("Zdefiniuj funkcję `rot13(text)` w module kartkowka4.py")
    exit()

try:
    kartkowka4.rot13('')
except TypeError:
    print("Funkcja `rot13()` powinna przyjmować jeden argument tekstowy.")
    exit()
except Exception as e:
    print("Wyjątek podczas wywołania `rot13('')`:")
    print(repr(e))
    exit()

score = 0

tests = [("", 10),
         ("A", 10),
         ("BACA", 10),
         ("N", 10),
         ("BOBO", 10),
         ]

print('Testy:')
print()
for i, (text, points) in enumerate(tests):
    print(i, 'rot13({})'.format(repr(text)))
    try:
        result = kartkowka4.rot13(text)
    except Exception as e:
        print('Nastąpił wyjatek:')
        print(repr(e))
        print('(0 punktów procentowych)')
    else:
        expected = encode(text, 'rot_13')
        if result == expected:
            print('Test zaliczony ({} punktów procentowych)'.format(points))
            score += points
        else:
            print('Błędny wynik')
            print('Oczekiwany wynik:')
            print(repr(expected))
            print('Otrzymany wynik:')
            print(repr(result))
            print('(0 punktów procentowych)')

    print()

print('Ocena minimalna: {}%'.format(score))
