from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    number = randint(1, 1000)
    question = number
    answer = is_even(number)
    if answer:
        right_answer = 'yes'
        return right_answer, question
    else:
        right_answer = 'no'
        return right_answer, question
