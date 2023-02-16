import prompt
from brain_games.cli import welcome_user


def brain_run(game_logic):
    name = welcome_user()
    print(game_logic.DESCRIPTION)
    n = 3
    while n >= 1:
        n -= 1
        right_answer, question = game_logic.get_question_and_answer()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
