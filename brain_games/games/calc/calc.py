from random import randint


def calc():
    global result
    number1 = randint(10, 100)
    number2 = randint(1, 10)
    operator_num = randint(1, 3)
    if operator_num == 1:
        print(f'Question: {number1} * {number2}')
        result = str(number1 * number2)
    elif operator_num == 2:
        print(f'Question: {number1} + {number2}')
        result = str(number1 + number2)
    else:
        print(f'Question: {number1} - {number2}')
        result = str(number1 - number2)
    
   
