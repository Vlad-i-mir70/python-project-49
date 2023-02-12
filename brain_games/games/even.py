from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0


def brain_even():
    number = randint(1, 1000)
    question = f'Question: {number}'
    answer = is_even(number)
    if answer:
        right_answer = 'yes'
        return right_answer, question
    else:
        right_answer = 'no'
        return right_answer, question
