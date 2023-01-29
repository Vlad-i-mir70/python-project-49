from random import randint


def brain_even():
    number = randint(1, 1000)
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = f'Question: {number}'

    def is_even(number):
        if number % 2 == 0:
            return 'yes'
        return 'no'
    result = is_even(number)
    return result, task, question
