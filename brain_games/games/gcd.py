from random import randint
import math


def brain_logic():
    number1 = randint(10, 99)
    number2 = randint(10, 99)
    task = 'Find the greatest common divisor of given numbers.'
    question = (f'Question: {number1} {number2}')

    def is_gcd(a, b):
        result = str(math.gcd(a, b))
        return result
    result = is_gcd(number1, number2)
    return result, task, question
