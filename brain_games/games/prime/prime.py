from random import randint
from math import sqrt


def brain_prime():
    number = randint(1, 1000)
    print(f' Question: {number}')
    i = 1
    if number == 3:
        return 'yes'
    while i < sqrt(number):
        i += 1
        if number % i == 0:
            return 'no'
    return 'yes'
