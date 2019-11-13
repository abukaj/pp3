#!/usr/bin/python3

def insertion_sort(sequence):
    for first_not_sorted in range(len(sequence) - 1):
        insert_to_sorted(sequence, first_not_sorted)
        # NIEZMIENNIK:
        # wszystkie elementy sequence o indeksach mniejszych od
        # first_not_sorted sa posortowane i nie wieksze od pozostalych
        # elementow


def insert_to_sorted(sequence, element_index):
    pass


if __name__ == '__main__':
    # numbers = []
    # insertion_sort(numbers)
    # assert numbers == []

    # numbers = [1]
    # insertion_sort(numbers)
    # assert numbers == [1]

    # numbers = [2, 1]
    # insertion_sort(numbers)
    # assert numbers == [1, 2]

    # numbers = [2, 1, 3]
    # insertion_sort(numbers)
    # assert numbers == [1, 2, 3]

