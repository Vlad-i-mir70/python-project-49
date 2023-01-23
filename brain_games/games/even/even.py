from random import randint


def brain_even():
    number = randint(1, 1000)
    print(f'Question: {number}')
    if number % 2 == 0:
        return 'yes'

    return 'no'
