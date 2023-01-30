from random import randint


def brain_prime():
    number = randint(1, 1000)
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = f' Question: {number}'

    def is_prime(number):
        if number == 1:
            return 'no'
        for i in range(2, number):
            if number % i == 0:
                return 'no'
        return 'yes'
    result = is_prime(number)
    return result, task, question
