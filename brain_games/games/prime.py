from random import randint
from math import sqrt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_nonprime(number):
    i = 1
    if number == 2:
        return number != 2
    while i < sqrt(number):
        i += 1
        if number % i == 0:
            return number % i == 0
    return number % i == 0


def get_question_and_answer():
    number = randint(1, 1000)
    answer = is_nonprime(number)
    return ('no', number) if answer else ('yes', number)
