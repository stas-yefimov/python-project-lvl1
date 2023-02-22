import random

MEMO = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    while number1 != number2:

        if number1 < number2:
            minimum = number1
            maximum = number2
        else:
            minimum = number2
            maximum = number1

        number1 = maximum - minimum
        number2 = minimum
    return number1


def get_question_and_answer():
    integer1 = random.randint(1, 100)
    integer2 = random.randint(1, 100)
    two_integers = f'{integer1} {integer2}'
    gcd = get_gcd(integer1, integer2)
    return two_integers, str(gcd)
