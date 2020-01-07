#!/usr/bin/python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    import re
    import sys
    if sys.version_info.major < 3:
        ModuleNotFoundError = ImportError

    import codecs
    encode = codecs.encode
    def doNotCheat(*args, **kwargs):
        raise RuntimeError("Nie korzystaj z codecs.encode()")
    
    codecs.encode = doNotCheat
    
    try:
        import kartkowka6 as kartkowka
    except (ModuleNotFoundError, ImportError):
        print("Zdefiniuj moduł kartkowka6.py")
        exit()
    except Exception as e:
        print("Błąd w module kartkowka6.py uniemożliwiający jego import:")
        print(repr(e))
        exit()
    

    if kartkowka.__doc__ is None:
        print("Brak napisu dokumentującego w module {.__name__}.py".format(kartkowka))
        exit()

    match = re.search('\\d\\d\\d\\d\\d\\d', kartkowka.__doc__)
    if match is None:
        print("Brak numeru albumu w napisie dokumentujacym")
        exit()
    student_id = match.group(0)
    
    try:
        f = kartkowka.inverted
    except AttributeError:
        print("Zdefiniuj funkcję `inverted(d)` w module {.__name__}.py".format(kartkowka))
        exit()

    try:
        f({})
    except TypeError:
        print("Funkcja `{.__name__}()` powinna móc przyjmować jeden argument typu dict.".format(f))
        exit()
    except Exception as e:
        print("Wyjątek podczas wywołania `{.__name__}({})`:".format(f))
        print(repr(e))
        exit()
    

    score = 0
    
    tests = [([{}],
               {},
               10),
             ([{0: 0}],
               {0: 0},
               10),
             ([{1: 2}],
               {2: 1},
               10),
             ([{'a': 1, 1: 'a'}],
               {'a': 1, 1: 'a'},
               10),
             ([{'a': 1, 2: 'b'}],
               {1: 'a', 'b': 2},
               10),
             ([[1, 2, 0]],
              {1: 0, 2: 1, 0: 2},
              150),
             ]
    
    print('Testy:')
    print('')
    for i, (args, expected, points) in enumerate(tests, 1):
        print('{}\t{.__name__}({})'.format(i, f, ', '.join(map(repr, args))))
            
        try:
            result = f(*args)
        except Exception as e:
            print('Nastąpił wyjatek:')
            print(repr(e))
            print('(0 punktów procentowych)')
        else:
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
    
        print('')
    
    print('Nr albumu: {}'.format(student_id))
    if score < 150:
        print('Ocena minimalna: {}%'.format(score))
    else:
        print('Ocena minimalna: {}%'.format(score - 150))
        print('Prowadzacy może przyznać do 150 punktów procentowych w zależności')
        print('od stopnia dodatkowego skomplikowania kodu.')
