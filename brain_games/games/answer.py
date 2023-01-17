import prompt

def answer():
    answer = prompt.string('Your answer: ')  
    lower_answer = answer.lower()
    if lower_answer == result:  
        print('Correct!')
    else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')