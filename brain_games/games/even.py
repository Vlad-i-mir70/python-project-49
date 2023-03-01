from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    number = randint(1, 1000)
    answer = is_even(number)
    return ('yes', number) if answer else ('no', number)
