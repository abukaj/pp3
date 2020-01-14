#!/usr/bin/python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    import re
    import sys
    if sys.version_info.major < 3:
        ModuleNotFoundError = ImportError

    import numpy
    def doNotCheat(*args, **kwargs):
        raise RuntimeError("Nie korzystaj z numpy.median()")
    
    numpy.median = doNotCheat
    
    try:
        import kartkowka7 as kartkowka
    except (ModuleNotFoundError, ImportError):
        print("Zdefiniuj moduł kartkowka7.py")
        exit()
    except Exception as e:
        print("Błąd w module kartkowka7.py uniemożliwiający jego import:")
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
        f = kartkowka.median
    except AttributeError:
        print("Zdefiniuj funkcję `median(iterable)` w module {.__name__}.py".format(kartkowka))
        exit()

    try:
        f([])
    except TypeError:
        print("Funkcja `{.__name__}()` powinna móc przyjmować jeden argument (iteratkę).".format(f))
        exit()
    except Exception as e:
        print("Wyjątek podczas wywołania `{.__name__}([])`:".format(f))
        print(repr(e))
        exit()
    

    score = 0
    
    tests = [([{}],
               None,
               10),
             ([[1]],
               1,
               10),
             ([(300, 2, -1)],
               2,
               10),
             ([[30, 10]],
               20,
               10),
             ([{15, 29, 1, 14, 20}],
              15,
              10),
             (['acb'],
              'b',
              75),
             ([(i for i in [11, 12, 890])],
              12,
              75),
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
                if points < 50:
                    print('Test zaliczony ({} punktów procentowych)'.format(points))
                else:
                    print('Test dodatkowy zaliczony')
                score += points
            else:
                print('Błędny wynik')
                print('Oczekiwany wynik:')
                print(repr(expected))
                print('Otrzymany wynik:')
                print(repr(result))
                print('(0 punktów procentowych)')
    
        print('')
    print('------------------------------------------')
    print()
    print('Nr albumu: {}'.format(student_id))
    print('Ocena minimalna: {}%'.format(score % 75))
    print()
    if score >= 75:
        print('Prowadzacy może przyznać dodatkowe punkty procentowe w zależności')
        print('od stopnia skomplikowania kodu.')
        print()
