from random import randint
from math import sqrt

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_nonprime(number):
    i = 1
    if number == 2:
        return number != 2
    while i < sqrt(number):
        i += 1
        if number % i == 0:
            return number % i == 0
    return number % i == 0


def brain_prime():
    number = randint(1, 1000)
    #task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = f' Question: {number}'
    answer = is_nonprime(number)
    if answer:
        right_answer = 'no'
        return right_answer, question
    else:
        right_answer = 'yes'
        return right_answer, question
