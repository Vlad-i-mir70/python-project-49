from random import randint
from random import choice
import operator


def brain_logic():
    number1 = randint(10, 100)
    number2 = randint(1, 10)
    operator_num = ['+', '-', '*']
    chuse_operator = choice(operator_num)
    task = 'What is the result of the expression?'
    question = f'Question: {number1} {chuse_operator} {number2}'
    if chuse_operator == '+':
        result = str(operator.add(number1, number2))
    elif chuse_operator == '-':
        result = str(operator.sub(number1, number2))
    else:
        result = str(operator.mul(number1, number2))
    return result, task, question
