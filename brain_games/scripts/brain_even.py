#!/usr/bin/env python3


from brain_games.games.even import brain_even
from brain_games.games.even import task
from brain_games.brain_engine import brain_run


def main():

    print(task)
    
    brain_run(brain_even)


if __name__ == "__main__":
    main()
