#!/usr/bin/env python3

from brain_games.brain_engine import brain_run
from brain_games.games.calc import brain_calc


def main():

    brain_run(brain_calc)


if __name__ == "__main__":
    main()
