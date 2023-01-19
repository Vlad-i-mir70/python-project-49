from brain_games.games.welcome import welcome
from brain_games.games.progression.progression import brain_progression
import prompt


def main():
    name = welcome()
    print('What number is missing in the progression?')
    n = 3
    while n >= 1:
        n -= 1
        resul = brain_progression()
        answ = prompt.string('Your answer: ')
        answ = int(answ)
        if answ == resul:
            print('Correct!')
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{resul}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
