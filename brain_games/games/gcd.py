import random


def init():
    print('Find the greatest common divisor of given numbers.')


def main():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    two_integers = f'{number1} {number2}'
    while number1 != number2:
        if number1 < number2:
            minimum = number1
            maximum = number2
        else:
            minimum = number2
            maximum = number1
        number1 = maximum - minimum
        number2 = minimum
    return two_integers, str(number1)
