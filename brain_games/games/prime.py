from random import randint
from math import sqrt


def brain_prime():
    number = randint(1, 1000)
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = f' Question: {number}'

    def is_prime(number):
        i = 1
        if number == 3:
            return 'yes'
        while i < sqrt(number):
            i += 1
            if number % i == 0:
                return 'no'
        return 'yes'
    result = is_prime(number)
    return result, task, question
