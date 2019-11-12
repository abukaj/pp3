#!/usr/bin/python3

def wait_for_password(password):
    while True:
        pass

if __name__ == '__main__':
    print('Wpisz haslo')
    wait_for_password('haslo')
    print('Brawo! A teraz zgadnij trudniejsze haslo')
    wait_for_password('hunter2')
    print('Brawo!')

