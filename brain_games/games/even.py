import random

MEMO = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 1000)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
