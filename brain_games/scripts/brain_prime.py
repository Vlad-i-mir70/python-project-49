#!/usr/bin/env python3

from brain_games.games.prime import brain_prime
from brain_games.games.prime import task
from brain_games.brain_engine import brain_run


def main():

    print(task)

    brain_run(brain_prime)


if __name__ == "__main__":
    main()
