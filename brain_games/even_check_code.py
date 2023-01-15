import prompt


from random import randint


def even_number():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 3
    while n >= 1:
        n -= 1
        number = randint(1, 1000)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        lower_answer = answer.lower()
        if number / 2 - int(number / 2) == 0:
            if lower_answer == 'yes':
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes' \nLet's try again, {name}!")
                return
        elif lower_answer == 'no':
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
