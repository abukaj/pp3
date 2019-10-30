#!/usr/bin/python3

def state_of_water_at(temperature):
    if temperature > 100:
        return 'gas'

    else:
        return 'liquid'


if __name__ == '__main__':
    assert state_of_water_at(10) == 'liquid'
    assert state_of_water_at(110) == 'gas'
    # assert state_of_water_at(-5) == 'solid'
