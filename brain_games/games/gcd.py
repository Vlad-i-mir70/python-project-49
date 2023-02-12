from random import randint
import math


task = 'Find the greatest common divisor of given numbers.'

def brain_gcd():
    number1 = randint(10, 99)
    number2 = randint(10, 99)
    question = (f'Question: {number1} {number2}')
    right_answer = str(math.gcd(number1, number2))
    return right_answer, question
