from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(numeric):
    return numeric % 2 == 0


def get_question_and_answer():
    numeric = randint(1, 1000)
    question = numeric
    answer = is_even(numeric)
    if answer:
        right_answer = 'yes'
        return right_answer, question
    else:
        right_answer = 'no'
        return right_answer, question
