import random


def init():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def is_even(number):
    return True if number % 2 == 0 else False


def main():
    number = random.randint(1, 1000)

    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
