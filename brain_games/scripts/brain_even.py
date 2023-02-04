#!/usr/bin/env python3

from brain_games.hello import welcome_user
from brain_games.even import game


def main():
    name = welcome_user()
    game(name)


if __name__ == '__main__':
    main()
