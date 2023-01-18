#!/usr/bin/env python3

from brain_games.games.welcome import welcome
from brain_games.games.gcd.gcd import gcd
import prompt


def main():
    name = welcome()
    print('What is the result of the expression?.')
    n = 3
    while n >= 1:
        n -= 1
        resul = gcd()
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
