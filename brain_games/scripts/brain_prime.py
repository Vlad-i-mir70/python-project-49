#!/usr/bin/env python3

from brain_games.games.welcome import welcome
from brain_games.games.prime.prime import brain_prime
import prompt


def main():
    name = welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = 3
    while n >= 1:
        n -= 1
        resul = brain_prime()
        answ = prompt.string('Your answer: ')
        lower_answer = answ.lower()
        if lower_answer == resul:
            print('Correct!')
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{resul}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()