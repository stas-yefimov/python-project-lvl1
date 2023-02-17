import random

MEMO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    number = random.randint(1, 1000)

    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'

    return number, answer
