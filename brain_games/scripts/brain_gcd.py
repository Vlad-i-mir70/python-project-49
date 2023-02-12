#!/usr/bin/env python3


from brain_games.games.gcd import brain_gcd
from brain_games.games.gcd import task
from brain_games.brain_engine import brain_run


def main():

    print(task)

    brain_run(brain_gcd)


if __name__ == "__main__":
    main()
