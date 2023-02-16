from random import randint
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1 = randint(10, 99)
    number2 = randint(10, 99)
    question = (f'{number1} {number2}')
    right_answer = str(math.gcd(number1, number2))
    return right_answer, question
