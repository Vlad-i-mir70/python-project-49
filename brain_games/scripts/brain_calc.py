#!/usr/bin/env python3

from brain_games.games.welcome import welcome
from brain_games.games.calc.calc import calc
from random import randint
import prompt

def main():   
    welcome()
    print('What is the result of the expression?.')
    n = 3
    while n >= 1:
        n -= 1
        calc()
        answer = prompt.string('Your answer: ')  
        lower_answer = answer.lower()
        if lower_answer == result:  
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {name}!")
         
        
    print(f'Congratulations, {name}!')

main()


if __name__ == "__main__":
    main()
