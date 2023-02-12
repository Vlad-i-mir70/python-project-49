from random import randint
from random import choice
import operator


task = 'What is the result of the expression?'


def make_question():
    number1 = randint(10, 100)
    number2 = randint(1, 10)
    operator_str = ['+', '-', '*']
    operator_random = choice(operator_str)
    question = f'Question: {number1} {operator_random} {number2}'
    return operator_random, question, number1, number2


def brain_calc():
    operator_random, question, number1, number2 = make_question()
    if operator_random == '+':
        right_answer = str(operator.add(number1, number2))
    elif operator_random == '-':
        right_answer = str(operator.sub(number1, number2))
    else:
        right_answer = str(operator.mul(number1, number2))
    return right_answer, question
