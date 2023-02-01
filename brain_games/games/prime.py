from random import randint


def is_nonprime(number):
    if number == 1:
        return number == 1
    else:
        for i in range(2, number):
            if number % i == 0:
                return number % i == 0
            else:
                return number % i == 0


def brain_prime():
    number = randint(1, 1000)
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = f' Question: {number}'
    answer = is_nonprime(number)
    if answer:
        result = 'no'
        return result, task, question
    else:
        result = 'yes'
        return result, task, question
