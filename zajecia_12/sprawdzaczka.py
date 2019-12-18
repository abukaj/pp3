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
        import kartkowka5 as kartkowka
    except (ModuleNotFoundError, ImportError):
        print("Zdefiniuj moduł kartkowka5.py")
        exit()
    except Exception as e:
        print("Błąd w module kartkowka5.py uniemożliwiający jego import:")
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
        f = kartkowka.gaderypoluki
    except AttributeError:
        print("Zdefiniuj funkcję `gaderypoluki(text, key='gaderypoluki')` w module {.__name__}.py".format(kartkowka))
        exit()

    try:
        f('')
    except TypeError:
        print("Funkcja `{.__name__}()` powinna móc przyjmować jeden argument tekstowy.".format(f))
        exit()
    except Exception as e:
        print("Wyjątek podczas wywołania `{.__name__}('')`:".format(f))
        print(repr(e))
        exit()
    
    try:
        kartkowka.gaderypoluki('', 'gaderypoluki')
    except TypeError:
        print("Funkcja `{.__name__}()` powinna móc przyjmować dwa argumenty tekstowe.".format(f))
        exit()
    except Exception as e:
        print("Wyjątek podczas wywołania `{.__name__}('', 'gaderypoluki')`:".format(f))
        print(repr(e))
        exit()

    score = 0
    
    tests = [([""],
               "",
               4),
             (["b"],
               "b",
               4),
             (["bz"],
               "bz",
               4),
             (["g"],
               "a",
               4),
             (["y"],
               "r",
               4),
             (["gaderypoluki"],
               "agedyropulik",
               4),
             (["B"],
               "B",
               2),
             (["BZW"],
               "BZW",
               2),
             (["A"],
               "G",
               4),
             (["P"],
               "O",
               4),
             (["AG-ED-YR OP-UL-IK tp iugsrcznr szrfy hgycdysik"],
               "GA-DE-RY PO-LU-KI to klasyczny szyfr harcerski",
               4),
             ([u"Wkduipść uktdy iulczg nkd opwknng mkdć zngczdnkg.", "GADERYPOLUKI"],
               u"Wielkość liter klucza nie powinna mieć znaczenia.",
              5),
             (["AM-IL-ON-EW UB-YT yn loot sztfr z rndzlot Gmdwrt Pnibkl.", "MalinoweButy"],
               "MA-LI-NO-WE BU-TY to inny szyfr z rodziny Gadery Poluki.",
              5),
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
    print('Ocena minimalna: {}%'.format(score))
