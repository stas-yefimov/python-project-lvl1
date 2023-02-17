import random

MEMO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:

        if number % divider == 0:
            return False

        divider += 1

    return True


def get_question_and_answer():
    number = random.randint(1, 100)

    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'

    return number, answer
