#!/usr/bin/env python3


from brain_games.brain_engine import brain_run
from brain_games.games.gcd import brain_gcd


def main():

    brain_run(brain_gcd)


if __name__ == "__main__":
    main()
