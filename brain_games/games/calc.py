from random import randint
from random import choice
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    number1 = randint(10, 100)
    number2 = randint(1, 10)
    operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    operator_random = choice(list(operator_dict))
    question = f'{number1} {operator_random} {number2}'
    operator_random_value = operator_dict[operator_random]
    right_answer = str(operator_random_value(number1, number2))
    return right_answer, question
